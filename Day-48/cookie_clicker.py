from selenium import webdriver 
from selenium.webdriver.common.by import By
import time 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,value="cookie")

def highestExtra():
    curr_cookie_score = int(driver.find_element(By.ID,value = "money").text)
    print(curr_cookie_score)
    highest_extra = None
    #check which extra to buy:
    if curr_cookie_score >=  123456789:
        highest_extra = driver.find_element(By.ID,value="buyTime machine")
    elif curr_cookie_score >=1000000:
        highest_extra = driver.find_element(By.ID,value="buyPortal")
    elif curr_cookie_score >=50000:
        highest_extra = driver.find_element(By.ID,value="buyAlchemy lab")
    elif curr_cookie_score >= 7000:
        highest_extra = driver.find_element(By.ID,value="buyShipment")
    elif curr_cookie_score >=2000:
        highest_extra = driver.find_element(By.ID,value="buyMine")
    elif curr_cookie_score >=500:
         highest_extra = driver.find_element(By.ID,value="buyFactory")
    elif curr_cookie_score >=100:
        highest_extra = driver.find_element(By.ID,value="buyGrandma")
    elif curr_cookie_score >=19:
        highest_extra = driver.find_element(By.ID,value="buyCursor")
    
    return highest_extra


        
        

        
        


isGameOn = True
curr_time = time.time()
curr_extras_time = time.time()

game_timeout = 60  #lets say we play the game for a minute that is 60 seconds..
buy_extras_timeout = 5  #lets say we buy an extra every 5 seconds....

while isGameOn:
    if time.time()>=curr_time + game_timeout:
        isGameOn = False 
        continue 

    cookie.click()
    #check if 5 seconds have passed
    if time.time() >= curr_extras_time + buy_extras_timeout:
        highest_extra = highestExtra()
        if highest_extra:
            highest_extra.click()
        curr_extras_time = time.time()
        

