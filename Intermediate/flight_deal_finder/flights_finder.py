import requests
import requests_cache
import os
from dotenv import load_dotenv

#Loading environment variables from .env file
load_dotenv()

SERP_API_ENDPOINT = "https://serpapi.com/search"


class Flights:
    """ This will be responsible for communication with google flights api"""
    def __init__(self):
        self.SERP_API = os.environ.get("SERP_API")
        

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "currency": "USD",
            "type": "1",
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "api_key": self.SERP_API,
        }

        response = requests.get(url=SERP_API_ENDPOINT, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code is {response.status_code}")
            return None
        
        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data


