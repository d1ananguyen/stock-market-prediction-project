import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt



#import AAPL csv, csv data is different from yahoo finance
csv_AAPL = pd.read_csv('individual_tickers/AAPL_historic.csv')
print(csv_AAPL.head())


#since date type is just a object convert it to a datetime object
csv_AAPL['Date'] = pd.to_datetime(csv_AAPL['Date'])

#check data type
print(csv_AAPL.info())
print(csv_AAPL.dtypes)

#After looking at data since volume is such a big number you need to scale out so model doesnt struggle
#print(csv_AAPL.describe().to_string())

#declare the features
features = ['Close','High','Low','Open','Volume']

#declare the type of scalar you're using
scaler = StandardScaler()
csv_AAPL[features] = scaler.fit_transform(csv_AAPL[features])

print(csv_AAPL.describe().to_string())

#this shows my plot as a symmetric plot
# for feat in features:
#     plt.figure()                # start a new figure for each feature
#     csv_AAPL[feat].hist(bins=30)      # you can tweak the number of bins
#     plt.title(f'Distribution of {feat}')
#     plt.xlabel(feat)
#     plt.ylabel('Frequency')
#     plt.show()


#drop unneeded values and then create a new csv
# drops Date (or any other non‑numeric columns) if you haven’t already
df_model = csv_AAPL.drop(columns=['Date'])

# save
df_model.to_csv('individual_tickers/scaled_data.csv', index=False)
print("Saved cleaned & scaled data to scaled_data.csv")



