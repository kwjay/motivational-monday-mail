import smtplib

user = "email@gmail.com"
password = "password"
quote = "xdd"


connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=user, password=password)
connection.sendmail(from_addr=user, to_addrs=user, msg=f"Subject:Motivational Quote\n\n{quote}")
connection.close()
