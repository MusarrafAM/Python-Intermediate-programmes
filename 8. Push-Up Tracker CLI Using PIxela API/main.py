import requests
import datetime as dt

USERNAME = "musarraf"
TOKEN = "&6A!92kF8skP#Or+"    # I generated this password.
GRAPH_ID = "graph2"
GRAPH_NAME = "Push-Up-Tracker"
UNIT = "Push-Ups"
TYPE = "int"
COLOUR = "shibafu"      # green = shibafu,  red = sora, purple = ajisai


# ----------------------------------1.Create an account--------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,   # Like password
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# -------------------------------2.Create a Graph---------------------------------------------
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": UNIT,
    "type": TYPE,
    "color": COLOUR,
}

header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)


# ------------------------------------------3.Create a pixel for the day-----------------------------------
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

now = dt.datetime.now()
formatted_today = now.strftime("%Y%m%d")


# pixel_data = {
#     "date": formatted_today,
#     "quantity": input("Enter how my push-ups you've done today:")
# }
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
# print(response.text)


# ------------------------------4.PUT / Update the pixel---------------------------------------------
CHANGE_DATE = 20230111
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{CHANGE_DATE}"

change_pixel_data = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_endpoint, json=change_pixel_data, headers=header)
# print(response.text)


# ---------------------------------------5.Delete a pixel-----------------------------------------------
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{CHANGE_DATE}"

# response = requests.delete(url=delete_pixel_endpoint, headers=header)
# print(response.text)


# ---------------------------------------6. Delete a Graph----------------------------------------
delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.delete(delete_graph_endpoint, headers=header)
# print(response.text)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Site url for check $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
check = "https://pixe.la/v1/users/musarraf/graphs/graph2.html"
