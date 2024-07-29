from selenium import webdriver 
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(price.text)

events_timings_tags = driver.find_elements(By.CSS_SELECTOR,value="div.event-widget div.shrubbery ul.menu li time")
events_titles_tags = driver.find_elements(By.CSS_SELECTOR,value="div.event-widget div.shrubbery ul.menu li a")

events = {}

for i in range(len(events_timings_tags)):
    events[i] = {
        "time":events_timings_tags[i].text,
        "name":events_titles_tags[i].text
    }

print(events)


driver.quit()



