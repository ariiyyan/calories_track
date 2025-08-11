import requests

GENER = "male"
WEIGHT_KG = 98
HEIGHT_CM = 183
AGE = 35

APP_ID = "5b0fbf4e"
API_KEY = "0bb9725a42ea4ef2457663e095e70655"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)