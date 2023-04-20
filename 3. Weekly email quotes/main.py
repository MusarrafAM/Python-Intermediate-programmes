import datetime as dt
import smtplib
import random

my_email = "musapython1@gmail.com"
my_password = "Use ur password here"  # this password get from mail evjmuhullfguaohg generated
sender_email = "musapython1@yahoo.com"

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 5:  # 0 == Monday
    for i in range(5):
        with open("quotes.txt") as file:
            quotes = file.readlines()

        random_quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=sender_email,
                                msg=f"Subject: Weekly quotes\n\n{random_quote}")
