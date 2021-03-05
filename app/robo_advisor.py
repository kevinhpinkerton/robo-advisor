#app/robo_advisor.py

import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import datetime as dt

def to_usd(price):
    return f"${price:,.2f}" 

print("Each ticker is inputted individually. Hit the return key once to continue, twice to finish.")

api_key = os.getenv("ALPHAVANTAGE_API_KEY")
columns = {'timestamp': str, 'open': float, 'high': float, 'low': float, 'close': float, 'volume': int}
risk_factor = .2
data = dict()

while True:
    ticker = input("Input a ticker: ").upper()
    if ticker == "":
        break
    elif len(ticker) < 1 or len(ticker) > 5 or not ticker.isalpha():
        print("Expecting a properly-formed stock symbol like 'MSFT'. Try again.")
    else:
        request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"
        try:
            response = requests.get(request_url)
            parsed_response = json.loads(response.text)

            df = pd.DataFrame.from_dict(parsed_response["Time Series (Daily)"], 'index')
            df.reset_index(inplace = True)
            df.columns = columns.keys()
            df = df.astype(columns)

            # df.to_csv(os.path.join(os.path.dirname(__file__), "..", "data", f"prices_{ticker.lower()}.csv"), index = False)

            if min(df['low']) * (1 + risk_factor) > df['close'][0]:
                recommendation = "BUY"
            else:
                recommendation = "DO NOT BUY"
                
            data[ticker] = {
                "LATEST DAY": df['timestamp'][0],
                "LATEST CLOSE": to_usd(df['close'][0]),
                "RECENT HIGH": to_usd(max(df['high'][:100])),
                "RECENT LOW": to_usd(min(df['low'])),
                "RECOMMENDATION": recommendation
            }
        except:
            print("Sorry, couldn't get any trading data for " + ticker + ".")

print("-------------------------")
print("SELECTED SYMBOLS: " + ", ".join(data.keys()))
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: {date:%Y-%m-%d %I:%M %p}".format(date=dt.datetime.now()))
print("-------------------------")
print(pd.DataFrame.from_dict(data, 'index'))
print("-------------------------")
print("Buy recommendations are issued if the stock's latest closing price is less than 20% above its recent low.")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")