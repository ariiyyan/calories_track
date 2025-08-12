import requests
from datetime import datetime

GENER = "male"
WEIGHT_KG = 98
HEIGHT_CM = 183
AGE = 35

APP_ID = "***"
API_KEY = "****"

exercise_endpoint = "****"
sheet_endpoint = "***"

exercise_text = input("Tell me which exercises you did: ")

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,

}

parameters = {
    "query": exercise_text,
    "gender": GENER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=header)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    print(sheet_response.text)







print(result)