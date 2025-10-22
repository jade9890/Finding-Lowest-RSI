import pandas as pd
import talib as ta
import yfinance as yf

#scrape wikipedia table
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
tables = pd.read_html(url)

#The first table contains the S&P 500 companies
sp500 = tables[0]


#Extract the symbols (tickers)
tickersList = sp500['Symbol'].tolist()


#download data for different intervals of time
oneDayData = yf.download(tickersList, period="max", interval="1d", group_by='ticker')
fourHourData = yf.download(tickersList, period ="1yr", intervals="4h", group_by='ticker')


#get close prices
closePrice1D = oneDayData.xs("Close", axis=1, level=1)
closePrice4Hr = fourHourData.xs("Close", axis=1, level=1)


#get rsi based on close prices
rsiOneDay = pd.DataFrame({ticker: ta.RSI(closePrice1D[ticker],timeperiod=14) for ticker in tickersList})
rsiFourHour = pd.DataFrame({ticker: ta.RSI(closePrice4Hr[ticker],timeperiod=14) for ticker in tickersList})