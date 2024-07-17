import smtplib
import datetime as dt 
import random

now = dt.datetime.now()
user = "avinaasha382@gmail.com"
password = ""

with open("quotes.txt",mode = "r") as fp:
    quotes = fp.readlines()




if now.weekday() == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        random_quote = random.choice(quotes)
        connection.starttls()
        connection.login(user = user, password=password)
        connection.sendmail(from_addr=user,to_addrs="vidyaa2005@gmail.com",msg = random_quote)

print("Finished...")