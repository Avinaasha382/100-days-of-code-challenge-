import requests
from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv()



account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)


message = client.messages.create(
  from_='+14842977148',
  to='+917200289315',
  body="Hiiii",
)



print(message.sid)


weather_params = {
    "lat":13.082680,
    "lon":80.270721,
    "appid":"03ecd436cad8e4aef242bd0342a3ff36",
    "cnt":1
}

res = requests.get(url = "https://api.openweathermap.org/data/2.5/weather",params=weather_params)
res.raise_for_status()
weather_data = res.json()

weather_id = []
weather_id = weather_data["weather"][0]["id"]
print(weather_id)

