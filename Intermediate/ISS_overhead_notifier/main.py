import requests
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()
from datetime import datetime

CURRENT_LATITUDE = 40.620718,
CURRENT_LONGITUDE = -75.378489


def is_iss_overhead():
    iss_data = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data.raise_for_status()
    iss_lon = float(iss_data.json()["iss_position"]["longitude"])
    iss_lat = float(iss_data.json()["iss_position"]["latitude"])

    if CURRENT_LATITUDE-5 <= iss_lat <= CURRENT_LONGITUDE+5 and CURRENT_LONGITUDE-5 <= iss_lon <= CURRENT_LONGITUDE+5:
        return True
    return False


def is_night():

    parameters = {
        "lat": 40.620718,
        "lng": -75.378489,
    }

    response = requests.get("https://api.sunrise-sunset.org/v2?", params=parameters)
    response.raise_for_status()
    # print(response.json())
    data = response.json()
    sunrise_time = int(data["sunrise"].split("T")[1].split("-")[0].split(":")[0])
    sunset_time = int(data["sunset"].split("T")[1].split("-")[0].split(":")[0])

    current_time = datetime.now().hour

    if current_time >= sunset_time or current_time <= sunrise_time:
        return True


# Look up if is_night and is_iss_overhead are true
while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
            connection.sendmail(from_addr=os.getenv("EMAIL"), 
                                to_addrs="ozodtech7@gmail.com",
                                msg=f"Subject: LOOK UP!\n\nThe International Space station is above you in the sky.")
    