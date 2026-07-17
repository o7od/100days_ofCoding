import requests
from datetime import datetime, timedelta
import requests_cache
import os
from dotenv import load_dotenv

requests_cache.install_cache("flight_deals")

class Flights:
    """ This will be responsible for communication with google flights api"""
    def __init__(self, departing_air: str):
        load_dotenv()
        self.SERP_API = os.environ.get("SERP_API")
        self.api_endpoint = "https://serpapi.com/search?engine=google_flights_deals"
        # call get_outbound_date
        self.get_outbound_date()
        self.departure_airport = departing_air
        self.parameters = {
            "departure_id": self.departure_airport,
            "currency": "USD",
            "api_key": self.SERP_API,
            "outbound_date": self.outbound_date,
        }

    def get_outbound_date(self):
        current_date = datetime.now()
        end_date = current_date + timedelta(30*6)
        begin_time = str(current_date).split(" ")[0]
        end_time = str(end_date).split(" ")[0]
        self.outbound_date = f"{begin_time},{end_time}"


    def find_deals(self):
        response = requests.get(url=self.api_endpoint, params=self.parameters)
        source: str = 'CACHE' if getattr(response, 'from_cache', False) else 'API'
        print(f"Source: {source}")
        if response.status_code == 200:
            return response.json()["deals"]
        return "couldn't fetch anything"