#app/robo_advisor.py

import re
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd

def TakeInput():

    user_ticker = input("Please input a ticker: ").lower()
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
df.columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']

# print(df)
df.to_csv(f"data/prices_{ticker}.csv", index = False)
