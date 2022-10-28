'''Fetches live prices of stocks with ticker symbols in excel sheet as input'''

import pandas_datareader as pdr
import pandas as pd
import yfinance as yf


def stock(ticker):
    '''Retrieving the live stock price'''

    print("\nFetching the data for {}...".format(ticker))
    stock_info = yf.Ticker(ticker).info
    market_price = stock_info['regularMarketPrice']
    close_price = stock_info['regularMarketPreviousClose']
    print("Ticker: " + ticker + "\nMarket Price: " + str(market_price) +
          " GBP\nPrevious Close Price: " + str(close_price) + " GBP\n")


stock_file = r"enter_the_location_of_the_excel_sheet_containing_the_list_of_required_ticker_symbols\stock_live_prices_list.xlsx"

sym = pd.read_excel(stock_file)
print("\n")
print(sym)

tick = sym['Tickers']

for i in range(0, len(tick)):
    stock(tick.iloc[i])
