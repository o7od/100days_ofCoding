import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


# Getting a quote 
def get_a_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()
    return quote


# Sending it to a person
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
    connection.sendmail(from_addr=os.getenv("EMAIL"),
                        to_addrs="kentneu8@gmail.com",
                        msg=f"Subject: Quote of the day\n\n{get_a_quote()}"
    )
    print("Successfully sent!")
