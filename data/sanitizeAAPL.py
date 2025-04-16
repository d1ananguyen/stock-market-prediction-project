import pandas as pd
from sklearn.preprocessing import StandardScaler


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


