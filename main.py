import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = "ID"
API_KEY = "KEY"
PASS = "PASS"
USER_ID = "USER"
GENDER = "your_gender"
WEIGHT_KG = "weight"
HEIGHT_CM = "height"
AGE = "age"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": USER_ID
}

exercise_params = {
    "query": input("What workout did you do today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionix_endpoint = f"{nutritionix_endpoint}/exercise"

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers)
result = response.json()
name_list = [result["exercises"][i]["name"] for i in range(len(result["exercises"]))]
duration_list = [result["exercises"][i]["duration_min"] for i in range(len(result["exercises"]))]
calories_list = [result["exercises"][i]["nf_calories"] for i in range(len(result["exercises"]))]


add_row_endpoint = "https://api.sheety.co/55da13abe6ac380a23c1148741ceb631/workoutTracking/лист1"

today = datetime.now()
format_date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
basic = HTTPBasicAuth('user', 'pass')

for activities in range(len(name_list)):
    row_params = {
        "лист1": {
            "date": format_date,
            "time": time,
            "exercise": name_list[activities].title(),
            "duration": duration_list[activities],
            "calories": calories_list[activities],
        }
    }
    response_sheet = requests.post(url=add_row_endpoint, json=row_params, auth=(USER_ID, PASS))
    print(response_sheet.text)
