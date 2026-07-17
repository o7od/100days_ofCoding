# This will handle api requests to sending sms messages (VONAGE API)
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

    def send_message(self, message: str):
        sms_msg = Sms(to=os.environ.get("MY_NUMBER"),
                    from_=os.environ.get("VONAGE_NUMBER"),
                    text=message)
        response = self.client.messages.send(sms_msg)
        print(response)


        