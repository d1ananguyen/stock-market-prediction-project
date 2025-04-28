import pandas as pd
import numpy as np
import joblib
import yfinance as yf

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#load data here/use yahoo api figure this out
#yahoo data group is using
ticker = "AAPL"
start  = "2017-01-01"
end    = "2025-01-01"
csv_AAPL = yf.download(ticker, start=start, end=end).reset_index()
# csv_AAPL = pd.read_csv('individual_tickers/AAPL_historic.csv') #if you want latest date change to yahoo csv
csv_AAPL['Date'] = pd.to_datetime(csv_AAPL['Date'])
features = ['Close','High','Low','Open','Volume']
scaler = StandardScaler()
csv_AAPL[features] = scaler.fit_transform(csv_AAPL[features])

#features for your final model
df_fe = csv_AAPL.copy()
df_fe['Close_lag1']   = df_fe['Close'].shift(1)
df_fe['MA_5']         = df_fe['Close'].rolling(5).mean().shift(1)
df_fe['Volatility_5'] = df_fe['Close'].rolling(5).std().shift(1)
df_fe['Weekday']      = df_fe['Date'].dt.weekday
df_fe['Weekday_sin']  = np.sin(2 * np.pi * df_fe['Weekday'] / 7)
df_fe['Weekday_cos']  = np.cos(2 * np.pi * df_fe['Weekday'] / 7)
df_fe.dropna(inplace=True)

#training and testing split
X = df_fe.drop(columns=['Date','Close'])
y = df_fe['Close'].to_numpy().ravel()
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False, random_state=42
)

#trained mlp model with 2018-2023 data
# mlp_model = MLPRegressor(
#     hidden_layer_sizes=(128,128),
#     alpha=1e-4,
#     activation='relu',
#     solver='adam',
#     learning_rate_init=0.01,
#     max_iter=200,
#     random_state=42,
#     verbose=True
# )

#using updated data
mlp_model = MLPRegressor(
    hidden_layer_sizes=(128,128,128), #the more data there is the more neurons needed, due to our features
    alpha=1e-4,
    activation='relu',
    solver='adam',
    learning_rate_init=0.01,
    max_iter=200,
    random_state=42,
    verbose=True
)
mlp_model.fit(X_train, y_train)

#mse scores
y_pred = mlp_model.predict(X_test)
print("Test MSE:", mean_squared_error(y_test, y_pred))
print("Test R²:",  r2_score(y_test, y_pred))

#save model using joblib
joblib.dump(mlp_model, 'mlp_model.pkl')  # your trained model
joblib.dump(scaler, 'scaler.pkl')        # your fitted scaler
print("Saved 'mlp_model.pkl' and 'scaler.pkl'")

