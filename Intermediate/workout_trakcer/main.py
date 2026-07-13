import requests
from datetime import datetime
import os
from dotenv import load_dotenv

nutrition_url = "https://app.100daysofpython.dev"

def get_nutrition_info(url: str, body: dict, header: dict) -> tuple:
    """supported activities: Running/Jogging, Swimming, Walking, Cycling, Weightlifting"""

    response = requests.post(url=f"{url}/v1/nutrition/natural/exercise", headers=header, json=body)
    print(response.status_code)
    info = response.json()["exercises"][0]
    return (info["name"], info["duration_min"], info["nf_calories"])


def get_workout_info(url: str, header: dict):
    """gets the current record of workout info"""
    response = requests.get(url=url, headers=header)
    print(response.status_code)
    return response.json()


def post_workout(url: str, header: dict, workout_type: str, duration: str, calories: str):
    """posts a new workout info in the workout tracker"""
    today_date: str = str(datetime.now().strftime("%d/%m/%Y"))
    today_time: str = str(datetime.now().strftime("%H:%M:%S"))

    body = {
        "workout": {
            'date': today_date, 
            'time': today_time,
            'exercise': workout_type,
            'duration': duration,
            'calories': calories,
        }
    }

    response = requests.post(url=url, headers=header, json=body)
    print(response.json())


# loading our environment variables
load_dotenv()

nutrition_body = {
    "query": "ran 5 miles", # required parameter
    "weight_kg": 60,
    "height_cm": 175,
    "age": 20,
    "gender": "male",
}

nutrition_header = {
    "x-app-id": os.environ.get("api_id"),
    "x-app-key": os.environ.get("api_key"),
}


human_input = input("Tell me what exercises you did today: ").lower()

if human_input:
    nutrition_body["query"] = human_input

    # 1. First get workout info
    n_info: tuple = get_nutrition_info(body=nutrition_body, header=nutrition_header, url=nutrition_url)
    # 2. post it in a worksheet

    sheety_header = {
        "Authorization": os.environ.get("SHEETY_TOKEN")
    }
    post_workout(url=os.environ.get("SHEETY_URL"), header=sheety_header, workout_type=n_info[0], duration=n_info[1], calories=n_info[2])