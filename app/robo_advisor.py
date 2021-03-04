#app/robo_advisor.py

import re
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import datetime as dt

def to_usd(price):
    return f"${price:,.2f}" 

def TakeInput():

    user_ticker = input("Please input a ticker: ").upper()
    if len(user_ticker) < 1 or len(user_ticker) > 5 or not user_ticker.isalpha():
        print("Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again.")
        user_ticker = TakeInput()

    return(user_ticker)

def CreateDataframe():

    ticker = TakeInput()

    api_key = os.getenv("ALPHAVANTAGE_API_KEY")
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"

    df = pd.DataFrame()
    try:
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)
        df = pd.DataFrame.from_dict(parsed_response["Time Series (Daily)"], 'index')
    except:
        print("Sorry, couldn't find any trading data for that stock symbol")
        df, ticker = CreateDataframe()

    return(df, ticker)

df, ticker = CreateDataframe()
df.reset_index(inplace=True)
columns = {'timestamp': str, 'open': float, 'high': float, 'low': float, 'close': float, 'volume': int}
df.columns = columns.keys()
df = df.astype(columns)

# print(df)
# df.to_csv(f"data/prices_{ticker.lower()}.csv", index = False)

print("-------------------------")
print("SELECTED SYMBOL: " + ticker)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: {date:%Y-%m-%d %I:%M %p}".format(date=dt.datetime.now()))
print("-------------------------")
print("LATEST DAY: " + df['timestamp'][0])
print("LATEST CLOSE: " + to_usd(df['close'][0]))
print("RECENT HIGH: " + to_usd(df['high'][0]))
print("RECENT LOW: " + to_usd(df['low'][0]))
print("-------------------------")
print("RECOMMENDATION: TODO")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")