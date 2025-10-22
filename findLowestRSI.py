import pandas as pd
import talib as ta
import yfinance as yf

#scrape wikipedia table
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
tables = pd.read_html(url)

#The first table contains the S&P 500 companies
sp500 = tables[0]


#Extract the symbols (tickers)
tickers = sp500['Symbol'].tolist()
