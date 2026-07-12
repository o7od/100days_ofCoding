import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv("twilio.env")

URL = "https://api.openweathermap.org/data/2.5/forecast"
LATITUDE = 40.610146
LONGITUDE = -75.378791

params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": os.environ.get("API_ID"),
    "units": "metric",
    "cnt": 4
}


response = requests.get(url=URL, params=params)
response.raise_for_status()
weather_data = response.json()["list"]


for each_day in weather_data:
    rain_or_not = int(each_day["weather"][0]["id"])
    if rain_or_not < 700:
        print("True")
        rain_strength = each_day["weather"][0]["description"]
        time_rain = each_day["dt_txt"]
        # print(f"Do not forget to bring an umbrella")

        # Sending an sms notification to our phone 
        account_sid = os.environ.get("SID")
        auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="whatsapp:+14848929589",
            from_="whatsapp:+17372583478",
            # message="It's going to rain tomorrow! Don't forget your umbrella ☔️",
            content_sid="It's going to rain tomorrow! Don't forget your umbrella ☔️",
        )

print(message.status)