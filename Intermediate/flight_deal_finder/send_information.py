# This will handle api requests to sending sms messages (VONAGE API)
import os
from dotenv import load_dotenv
from vonage import Auth, Vonage
from vonage_messages import Sms
import smtplib


class NotificationManager:
    def __init__(self):
        load_dotenv()
        self.email = os.environ.get("MY_EMAIL")
        self.password = os.environ.get("MY_PASSWORD")
        self.client = Vonage(
            Auth(
                api_key=os.environ.get("VONAGE_API_KEY"),
                api_secret=os.environ.get("VONAGE_API_SECRET"),
            )
        )
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)

    def send_message(self, message: str):
        sms_msg = Sms(to=os.environ.get("MY_NUMBER"),
                    from_=os.environ.get("VONAGE_NUMBER"),
                    text=message)
        response = self.client.messages.send(sms_msg)
        print(response)

    def send_emails(self, message: str, customer_emails):
        print("Sending an email to customers")
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.password)
            for email in customer_emails:
                self.connection.sendmail(from_addr=self.email, 
                                    to_addrs=email,
                                    msg=f"Subject: Low Price Alert! \n\n{message}".encode('utf-8'))
                print("Successfully sent")


        