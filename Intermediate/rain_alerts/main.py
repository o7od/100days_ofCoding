import requests
from datetime import datetime
import os
from twilio.rest import Client
from dotenv import load_dotenv



api_id = "da0bd497992c76165a41bf148aa12e3f"
URL = "https://api.openweathermap.org/data/2.5/forecast"
LATITUDE = 40.610146
LONGITUDE = -75.378791

params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": api_id,
    "units": "metric",
    "cnt": 4
}


response = requests.get(url=URL, params=params)
response.raise_for_status()
weather_data = response.json()["list"]


for each_day in weather_data:
    rain_or_not = int(each_day["weather"][0]["id"])
    if rain_or_not < 700:
        rain_strength = each_day["weather"][0]["description"]
        time_rain = each_day["dt_txt"]
        # print(f"Do not forget to bring an umbrella")


        # Sending an sms notification to our phone 
        load_dotenv("twilio.env")
        account_sid = os.environ.get("SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="whatsapp: +998946124662",
            from_="whatsapp: +17372583478",
            body="It's going to rain tomorrow! Don't forget your umbrella ☔️",
        )

print(message.status)