import requests
import requests_cache
import os
from dotenv import load_dotenv

# requests_cache.install_cache('travels_info')


class Sheety_api:
    """This module will be responsible for communication with SHEETY API"""
    def __init__(self):
        load_dotenv()
        self.api_endpoint = os.environ.get("SHEETY_API")
        self.header = {
            "Authorization": os.environ.get("SHEETY_TOKEN"),
            "Content-Type": "application/json",
        }

    def post(self, travel_destination: dict):
        """posts a new information to the google sheets database"""
        body = {
            "price": {
                "city": travel_destination["city"],
                "iataCode": travel_destination["airport_code"],
                "lowestPrice": travel_destination["price"] if travel_destination["price"] != None else "10000",
            }
        }
        response = requests.post(url=self.api_endpoint, json=body, headers=self.header)
        source: str = 'CACHE' if getattr(response, 'from_cache', False) else 'API'
        print(f"Source: {source}")
        if response.status_code == 200:
            print("Successfully added a new travel destination!")
        else:
            print("Operation Unsuccessful!")

    def get(self) -> dict:
        """retrieves all the information in the google sheets database"""
        response = requests.get(url=self.api_endpoint, headers=self.header)
        source: str = 'CACHE' if getattr(response, 'from_cache', False) else 'API'
        print(f"Source: {source}")
        if response.status_code != 200:
            print("Unable to fetch any data!")
        return response.json()
    

    def update(self, object_id: int, new_price: str):
        """updates the given row with the object id"""
        new_body = {
            "price": {
                "lowestPrice": new_price,
            }
        }
        response = requests.put(url=f"{self.api_endpoint}/{object_id}", json=new_body, headers=self.header)
        return response.json()




    
