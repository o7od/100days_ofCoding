import requests
from datetime import datetime
import random
import os
from dotenv import load_dotenv
load_dotenv()

API_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get("USERNAME")
GRAPH_ID = os.environ.get("GRAPH_ID")
TOKEN = os.environ.get("MY_TOKEN")



data = {
    "token": os.environ.get("MY_TOKEN"), 
    "username": os.environ.get("USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # 1. Creating a Pixela user
def create_pixela_account(user_data: dict) -> bool:
    """creates a pixela accoutn"""
    response = requests.post(url=os.environ.get("API_ENDPOINT"), json=user_data)
    return response.json()
        

# 2. Updating my Pixela account
def update_profile(username: str):
    """returns the status of the put request"""
    url = f"https://pixe.la/@{username}"
    headers = {
    "X-USER-TOKEN": os.getenviron("MY_TOKEN")
    }

    put_data = {
        "displayName": "O-ozod",
        "gravatarIconEmail": "ozodotamirzayev@gmail.com",
        "title": "spiderman",
        "timezone": "US/Eastern",
        "contributeURLs": "https://github.com/o7od",

    }
    response = requests.put(url=url, headers=headers, json=put_data)
    return response.text


# 3. Viewing user profile
def view_profile(username: str):
    """returns a html code of the website"""
    url = f"https://pixe.la/@{username}"
    response = requests.get(url=url)
    return response.text


# 4. Creating a graph
def create_graph(username: str, x_user_token: str):
    """creates a graph on pixela given the user's account"""
    url = f"{API_ENDPOINT}/{username}/graphs"
    header = {
        "X-USER-TOKEN": x_user_token
    }
    request_body = {
        "id": "fight-club1",
        "name": "Workout Tracker",
        "unit": "day",
        "type": "int",
        "color": "ajisai",
        "timezone": "US/Eastern",
        "startOnMonday": True,

    }
    response = requests.post(url=url, headers=header, json=request_body)
    return response.text


def update_graph(username: str, x_user_token: str, body: dict, graphID: str):
    """updates the graph with specified change"""
    url = f"{API_ENDPOINT}/{username}/graphs/{graphID}"

    header = {
        "X-USER-TOKEN": x_user_token,
    }

    response = requests.put(url=url, headers=header, json=body)
    return response.text


# 5. Get a graph svg
def get_graph_svg(username: str, graphID: str):
    """gets a graph svg"""
    url = f"{API_ENDPOINT}/{username}/graphs/{graphID}"

    # request_body = {
    #     "mode": "short",
    #     "appearance": "dark",
    # }

    response = requests.get(url=url)
    return response.status_code


# # 6. Post a pixel
def post_pixel(username: str, graphID: str, x_user_token: str):
    url = f"{API_ENDPOINT}/{username}/graphs/{graphID}"
    today = datetime.now()
    date = today.strftime("%Y%m%d")

    header = {
    "X-USER-TOKEN": x_user_token
    }

    body = {
        "date": date,
        "quantity": str(random.randint(1, 10))
    }

    response = requests.post(url=url, headers=header, json=body)
    print(response.status_code)


# 7. Delete a pixel
def delete_pixel(username: str, graphID: str, x_user_token: str, date: str):
    url = f"{API_ENDPOINT}/{username}/graphs/{graphID}/{date}"
    header = {
        "X-USER-TOKEN": x_user_token,
    }

    response = requests.delete(url=url, headers=header)
    return response.status_code



print(delete_pixel(username=USERNAME, graphID=GRAPH_ID, x_user_token=TOKEN, date="20260615"))