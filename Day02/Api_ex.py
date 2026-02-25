import requests
API_KEY = "0P5YOG51CJ9HGTKY"

api_url = "https://www.alphavantage.co/"


def get_stock_market_data(symbol):
            query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
            response = requests.get(url= api_url + query)
            for key,value in response.json().items():
                if key == "Time Series (Daily)":
                        continue
                else:
                        print(key, value)
                

symbol = input ("ENTER THE SYMBOL FOR STOCK MARKET E.G IBM, AMZN, GOOGLE")
get_stock_market_data(symbol)







