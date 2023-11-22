import smtplib
import random
import datetime as dt

user = "email@gmail.com"
password = "password"
current_weekday = dt.datetime.now().weekday()

# 0 as Monday
if current_weekday == 0:
    with open("quotes.txt") as file:
        quote = random.choice(file.readlines())
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.sendmail(from_addr=user, to_addrs=user, msg=f"Subject:Motivational Quote\n\n{quote}")