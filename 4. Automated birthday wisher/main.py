import random
import pandas
import datetime as dt
import smtplib

PLACEHOLDER = "[NAME]"

my_email = "musapython1@gmail.com"
my_password = "ENTER YOUR PASSWORD HERE"   # this password get from mail  generated
sender_email = "musapython1@yahoo.com "

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# find today.
now = dt.datetime.now()
current_month = now.month
current_day = now.day


for each in data_dict:
    b_month = each["month"]
    b_day = each["day"]
    b_name = each["name"]
    b_email = each["email"]
    if b_month == current_month and b_day == current_day:
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
            message = file.read()
            final_message = message.replace(PLACEHOLDER, b_name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=sender_email,
                                    msg=f"Subject:Happy Birthday\n\n{final_message}")






# ########### Angelas code############ with dict comprehention and Dataframe iteration.kinda complex version.
# #                 #To run and test the code you need to update 4 places:
# # # 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# # # 2. Go to your email provider and make it allow less secure apps.
# # # 3. Update the SMTP ADDRESS to match your email provider.
# # # 4. Update birthdays.csv to contain today's month and day.
# # # See the solution video in the 100 Days of Python Course for explainations.


# from datetime import datetime
# import pandas
# import random
# import smtplib

# MY_EMAIL = "YOUR EMAIL"
# MY_PASSWORD = "YOUR PASSWORD"

# today = datetime.now()
# today_tuple = (today.month, today.day)

# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     birthday_person = birthdays_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", birthday_person["name"])

#     with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=birthday_person["email"],
#             msg=f"Subject:Happy Birthday!\n\n{contents}"
#         )



