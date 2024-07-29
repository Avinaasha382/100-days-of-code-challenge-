from bs4 import BeautifulSoup
import requests
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def fillForm(house_link,house_price,house_address):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options = chrome_options)
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScSAa5KoEff-NoMcijCMUEneqaTGHRpbfPm6dm7zXgsvB_xAg/viewform")
        
        wait = WebDriverWait(driver, 10)
        input_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.whsOnd")))
        
        # Get all input elements once the first is visible
        input_elements = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd")

        time.sleep(10)
        

        input_elements[0].send_keys(house_address)
        input_elements[1].send_keys(house_price)
        input_elements[2].send_keys(house_link)

        submit_button = driver.find_element(By.CSS_SELECTOR,value="span.l4V7wb span.NPEfkd")
        submit_button.click()
    except:
        print("Too fast")
    
    driver.quit()
    
    
    
website_data = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
soup = BeautifulSoup(website_data,"html.parser")

house_links_tags = soup.select(selector="a.property-card-link")
house_links = []

for tag in house_links_tags:
    house_links.append(tag.get("href"))


price_tags = soup.select(selector="div.PropertyCardWrapper span")
prices = []

for tag in price_tags:
    price_text = tag.getText()
    price = (price_text.split("+")[0].split("/")[0])
    prices.append(price)

address_tags = soup.select(selector="address")
address = []

for tag in address_tags:
    text = tag.getText().strip("\n").strip()
    final_address = ""
    for c in text:
        if c != '|':
            final_address+=c
    address.append(final_address)

print(address)

for i in range(len(house_links)):
    fillForm(house_links[i],prices[i],address[i])




