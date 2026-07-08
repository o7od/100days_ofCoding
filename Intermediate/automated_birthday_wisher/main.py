import pandas
from datetime import datetime
import smtplib
import random
import os
from dotenv import load_dotenv

load_dotenv()

# my email and password
my_email = os.getenv("EMAIL")
my_password = os.getenv("PASSWORD")


# Getting today's month and day, year
today = datetime.now()
today_year = today.year
today_day = today.day
today_month = today.month

# Reading family.csv data and checking against today's date
birthday_list = pandas.read_csv("family.csv")
for index, data in birthday_list.iterrows():
    month = data["month"]
    day = data["day"]
    year = data["year"]
    email_to_send = data["email"]
    name = data["Name"]

    # Preparing a subject title if there is any birthdays today
    if month == today_month and day == today_day:
        new_age = today_year - year
        subject_head = f"Subject: Congratulations on turning {new_age}\n\n"

        # Preparing a birthday text
        num = random.randint(1, 5)
        with open(f"birthday{num}.txt") as file:
            birthday_text = file.read().replace("[name]", name)
    
        # Sending it to their email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_to_send,
                                msg=subject_head + f"{birthday_text}")
        print("Succesfully Sent! ")
            
