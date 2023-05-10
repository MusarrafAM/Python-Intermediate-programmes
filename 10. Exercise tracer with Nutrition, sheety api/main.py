import requests
import datetime as dt


now = dt.datetime.now()
DATE_NOW = now.date().strftime("%d/%m/%Y")
TIME_NOW = now.time().strftime("%H:%M:%S")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_ID = "906be036"
NUTRITIONIX_API_KEY = "76601ae571f34f4f24496b29f2a4fae0"
exercise_text = input("Enter the exercise you did: ")

sheety_endpoint = "https://api.sheety.co/b3fe9090214a9e18fc363b736bbce157/myWorkouts/workouts"
# Above endpoint has username project name Sheetname

#  Optional params for NUTRITIONIX
GENDER = "male"
# WEIGHT_KG = YOUR WEIGHT
# HEIGHT_CM = YOUR HEIGHT
AGE = 23

nutrionox_exersice_parameters = {
    "query": exercise_text,   # compulsory
    "gender": GENDER,
    "age": AGE,
    #"weight_kg": WEIGHT_KG,
    #"height_cm": HEIGHT_CM,

}

header = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
}


responses = requests.post(url=exercise_endpoint, json=nutrionox_exersice_parameters, headers=header)
responses.raise_for_status()
data = responses.json()["exercises"]

for exercise in data:
    sheet_inputs = {
        "workout": {
            "date": DATE_NOW,
            "time": TIME_NOW,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": "Bearer musapythontoken"
    }

    sheet_responses = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=bearer_headers)
    print(sheet_responses.text)

# go to this link for updated sheet = "https://docs.google.com/spreadsheets/d/19H4GoT93yQ-jafULt_xo7CrpbC3cmDBP_SUEaG41rBU/edit#gid=0"

# Typical input ran 5k and cycle 20 mins


# -----------------------Authentication methods------------------------
# # we have to put our user name and password to the sheets for basic authentication
# # we have to put our secret Bearer (Token) for Bearer authentication.
# # 1. No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
# # 2. Basic Authentication
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         YOUR USERNAME,
#     YOUR PASSWORD,
#     )
# )
#
# # 3. Bearer Token Authentication
# bearer_headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )


