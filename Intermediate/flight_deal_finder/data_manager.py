import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DataManager:

    """This module will be responsible for communication with SHEETY API"""
    def __init__(self):
        self.prices_api_endpoint = os.environ.get("PRICES_SHEETY_API")
        self.users_api_endpoint = os.environ.get("USERS_SHEETY_API")
        self.header = {
            "Authorization": os.environ.get("SHEETY_TOKEN"),
            "Content-Type": "application/json",
        }
        self.destination_data = {}


    def get_destination_data(self) -> dict:
        """retrieves all the information in the google sheets database"""
        response = requests.get(url=self.prices_api_endpoint, headers=self.header)
        if response.status_code != 200:
            print("Unable to fetch any data!")
        self.destination_data = response.json()["prices"]
        return self.destination_data
    

    def update_lowest_price(self, object_id: int, new_price: str):
        """updates the given row with the object id"""
        new_body = {
            "price": {
                "lowestPrice": new_price,
            }
        }
        response = requests.put(url=f"{self.prices_api_endpoint}/{object_id}", json=new_body, headers=self.header)
        return response.json()

    def get_customer_emails(self):
        """gets customer emails from users list"""
        response = requests.get(url=self.users_api_endpoint, headers=self.header)
        return response.json()["users"]
        
    
