import requests
import datetime as dt
from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)



stock_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":os.getenv("stock_appid")
}

news_params = {
    "q":"tesla",
    "apiKey":os.getenv("news_appid")
}

yesterday = str(dt.date.today() - dt.timedelta(days = 2))
day_before_yesterday = str(dt.date.today() - dt.timedelta(days = 3))
day = str(dt.date.today())




response = requests.get(url = "https://www.alphavantage.co/query",params = stock_params)

print(response.status_code)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]

prev_data = float(stock_data[yesterday]["4. close"])
day_prev_data = float(stock_data[day_before_yesterday]["4. close"])

response = requests.get(url = "https://newsapi.org/v2/top-headlines",params = news_params)
news_data = response.json()["articles"]

percentage_difference = (abs(prev_data - day_prev_data)*100)/prev_data

top_news = (news_data[0],news_data[1],news_data[2])

#if decrease in stock price:

symbol = "🔺" if prev_data >= day_prev_data else "🔻"


message = client.messages.create(
    from_='+14842977148',  # Replace with your Twilio phone number
    to='+917200289315',  # Replace with recipient number
    body=f"{STOCK} {symbol} {percentage_difference}\n"
         f"Headline: {top_news[0]['title']}\n"
         f"Brief: {top_news[0]['description']}\n"
         f"Headline: {top_news[1]['title']}\n"
         f"Brief: {top_news[1]['description']}\n"
         f"Headline: {top_news[2]['title']}\n"
         f"Brief: {top_news[2]['description']}\n"
)

print(message.sid)







