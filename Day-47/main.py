import requests 
from bs4 import BeautifulSoup
import smtplib
import dotenv 
import os 

dotenv.load_dotenv()

SMTP_PASSWORD = os.getenv("smtp_password")
USER = "avinaasha382@gmail.com"

headers = {
    "Accept-Language":"en-US",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

def send_email(contents):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=USER,password=SMTP_PASSWORD)
    connection.sendmail(from_addr=USER,to_addrs="vidyaa2005@gmail.com",msg=contents.encode("utf-8"))
    connection.close()

response = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",headers=headers)
website_data = response.text



soup = BeautifulSoup(website_data,"html.parser")

price = int(soup.find(name="span",class_="a-price-whole").getText().split(".")[0])

print(price)

product_list = soup.select_one(selector="span#productTitle").getText().split("\n")

for i in range(len(product_list)):
    product_list[i] = product_list[i].strip()

product_title = ""

for item in product_list:
    product_title+=item 

print(product_title)

if price<100:
    contents = f"{product_title} now for ${price} \n  at https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
    send_email(contents=contents)


# # if price < 100:
# #     contents = f"{product_title} now for ${price} \n at https://appbrewery.github.io/instant_pot/"
# #     send_email(contents=contents)





