import pandas as pd

#import AAPL csv, csv data is different from yahoo finance
csv_AAPL = pd.read_csv('individual_tickers/AAPL_historic.csv')
print(csv_AAPL.head())


#since date type is just a object convert it to a datetime object
csv_AAPL['Date'] = pd.to_datetime(csv_AAPL['Date'])

#check data type
print(csv_AAPL.info())
print(csv_AAPL.dtypes)

#scale the data step 5 chatgpt then save or use clean data
