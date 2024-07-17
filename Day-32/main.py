##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt 
import random
import pandas as pd 

#2
now = dt.datetime.now()
curr_month = now.month
curr_day = now.day

user = "avinaasha382@gmail.com"
password = "" 

print(curr_month)
print(curr_day)

df = pd.read_csv("birthdays.csv")
data = df.to_dict(orient="records")
print(data)
for records in data:
    if records["month"] == curr_month and records["day"] == curr_day:
        letter_index = random.randint(1,3)

        #read a random letter template
        with open(f"./letter_templates/letter_{letter_index}.txt") as fp:
            letter_contents = fp.read()
            letter_contents = letter_contents.replace("[NAME]",records["name"])
        
        #send an email wishing them a happy birthday
        
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = user,password=password)
            connection.sendmail(from_addr=user,to_addrs=records["email"],msg = letter_contents)

print("Connections closed")






