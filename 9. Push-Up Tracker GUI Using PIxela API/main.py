import webbrowser
import requests
import datetime as dt
from tkinter import *
import messagebox

USERNAME = "musarraf"
TOKEN = "&6A!92kF8skP#Or+"  # I generated this password.
GRAPH_ID = "graph2"
GRAPH_NAME = "Push-Up-Tracker"
UNIT = "Push-Ups"
TYPE = "int"
COLOUR = "shibafu"  # green = shibafu,  red = sora, purple = ajisai

COLOUR_CHANGE_WAIT_TIME = 1000  # (1000 = 1 sec)

# ----------------------------------1.Create an account--------------------------------------
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,  # Like password
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

today = dt.datetime.now()
formatted_today = today.strftime("%Y%m%d")
yesterday = today - dt.timedelta(days=1)
formatted_yesterday = yesterday.strftime("%Y%m%d")

def click_submit():
    count = entry_count.get()
    date = date_entry.get()
    if count == "":
        messagebox.showinfo(title="Empty ERROR", message="push-ups cannot be empty.(put 0 for rest day)")
    elif date == "":
        messagebox.showinfo(title="Empty ERROR", message="date cannot be empty.")

    else:
        pixel_data = {
            "date": date,  # formatted_today,
            "quantity": count,
        }

        response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
        response_message = response.json()["message"]
        if response_message == "Success.":
            response_label_answer.config(text=response_message, bg="green")
        else:
            response_label_answer.config(text="Something went wrong,Try again", bg="red")
        print(response_message)
        window.after(COLOUR_CHANGE_WAIT_TIME, default_text)


# -----my decision we can update a pixel using create pixel at that day that will replace older pixel --------------
# ------------------------------4.PUT / Update the pixel#---------------------------------------------
CHANGE_DATE = 20230112
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{CHANGE_DATE}"

change_pixel_data = {
    "quantity": "10"
}

# response = requests.put(url=update_pixel_endpoint, json=change_pixel_data, headers=header)
# print(response.text)


# ---------------------------------------5.Delete a pixel-----------------------------------------------

def click_delete():
    date = date_entry.get()
    if date == "":
        messagebox.showinfo(title="Empty ERROR", message="date cannot be empty.")
    else:
        delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

        response = requests.delete(url=delete_pixel_endpoint, headers=header)
        response_message = response.json()["message"]
        if response_message == "Success.":
            response_label_answer.config(text=response_message, bg="green")
        elif response_message == "Specified pixel not found.":
            response_label_answer.config(text="There is no pixel on that day.", bg="orange")
        else:
            response_label_answer.config(text="Something went wrong,Try again", bg="red")
        print(response_message)
        window.after(COLOUR_CHANGE_WAIT_TIME, default_text)


# ---------------------------------------6. Delete a Graph----------------------------------------
delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.delete(delete_graph_endpoint, headers=header)
# print(response.text)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$Site url for check $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
check = "https://pixe.la/v1/users/musarraf/graphs/graph2.html"

# ##########################################     GUI     #############################################


url_for_habit_checker = "https://pixe.la/v1/users/musarraf/graphs/graph2.html"


def link_for_my_journey():
    webbrowser.open_new_tab(url_for_habit_checker)


def today_button():
    date_entry.delete(0, END)
    date_entry.insert(0, formatted_today)


def yesterday_button():
    date_entry.delete(0, END)
    date_entry.insert(0, formatted_yesterday)


def default_text():
    response_label_answer.config(text="Response will show up here", bg="grey")


window = Tk()
window.config(padx=50, pady=50)
window.title("Push-UP_Tracker")

label_for_push_up = Label(text="Push-Ups count: ")
label_for_push_up.grid(column=0, row=0)

entry_count = Entry(width=10)
entry_count.grid(column=1, row=0)

label_for_date = Label(text="Date: ")
label_for_date.grid(column=0, row=1)

date_entry = Entry()
date_entry.grid(column=1, row=1)

button_today = Button(text="Today", command=today_button)
button_today.grid(column=2, row=1)

button_yesterday = Button(text="Yesterday", command=yesterday_button)
button_yesterday.grid(column=3, row=1)

button_delete = Button(text="Delete", command=click_delete, bg="red")
button_delete.grid(column=0, row=3)

button_submit = Button(text="Submit", command=click_submit, bg="green")
button_submit.grid(column=1, row=3)

my_journey_button = Button(text="My journey", command=link_for_my_journey, bg="blue", width=14)
my_journey_button.grid(column=2, row=3, columnspan=3)

message_label = Label(text="This can be used\nfor update too")
message_label.grid(column=1, row=4)

response_label = Label(text="Response: ")
response_label.grid(column=0, row=5)

response_label_answer = Label(text="Response will show up here", width=30)
response_label_answer.grid(column=1, row=5)

window.mainloop()
