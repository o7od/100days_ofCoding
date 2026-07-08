from datetime import datetime
import random
import smtplib

my_email = "ozodotamirzaev06@gmail.com"
password = "lmldfhwkmmelzzeb"

# 2. Check if the current day is a particular weekday
today = datetime.now()
week_day = today.strftime("%a")

if week_day == "Wed":
    # 1. Turn the quotes into a list
    with open("quotes.txt", "r") as quotes_reader:
        content = [n.strip() for n in quotes_reader.readlines()]
        quote_of_the_day = random.choice(content)
    # 3. Send an email accordingly
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="ozodtech7@gmail.com", 
                            msg=f"Subject: Quote of the day\n\n{quote_of_the_day}"
        )
