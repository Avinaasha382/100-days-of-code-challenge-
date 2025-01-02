from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://fcainfoweb.nic.in/reports/report_menu_web.aspx")

price_button = driver.find_element(By.ID,value="ctl00_MainContent_Rbl_Rpt_type_0")
price_button.click()

time.sleep(5)

dropdown = driver.find_element(By.NAME,value="ctl00$MainContent$Ddl_Rpt_Option0")
dropdown.click()

options = dropdown.find_elements(By.TAG_NAME,value="option")
print(options)

options[1].click()

time.sleep(5)

input_date = driver.find_element(By.NAME,value="ctl00$MainContent$Txt_FrmDate")
input_date.send_keys("29/08/2024")

time.sleep(2)

submit_button = driver.find_element(By.NAME,value="ctl00$MainContent$btn_getdata1")
submit_button.click()

time.sleep(5)

print("Hello")

t = driver.find_elements(By.CSS_SELECTOR,value="tr")
print(t)
print("Yes")
print(t[0].tag_name)

td_elements = t[0].find_elements(By.TAG_NAME,value="td")

for ele in t:
    td_elements = ele.find_elements(By.TAG_NAME,value="td")
    data = []
    for td in td_elements:
        data.append(td.text)
    print(data)






