# This will handle api requests to sending sms messages (VONAGE API)
import requests
import os
from dotenv import load_dotenv
from vonage import Auth, Vonage
from vonage_messages import Sms


class Sms_sender:
    def __init__(self):
        load_dotenv()
        self.client = Vonage(
            Auth(
                api_key=os.environ.get("VONAGE_API_KEY"),
                api_secret=os.environ.get("VONAGE_API_SECRET"),
            )
        )


        # self.url = "https://messages-sandbox.nexmo.com/v1/messages"
        # self.payload = {
        #     "from": os.environ.get("WHATSAPP_SENDER_ID"),
        #     "to": "14848929589",
        #     "message_type": "text",
        #     "text": "This is a WhatsApp Message sent from the Messages API",
        #     "channel": "whatsapp"
        # }
        # self.header = {
        #     "Content-Type": "application/json",
        #     "Accept": "application/json"
        # }


    def send_message(self, message: str):
        sms_msg = Sms(to="14848929589",
                    from_=os.environ.get("VONAGE_NUMBER"),
                    text=message)
        response = self.client.messages.send(sms_msg)
        print(response)


        