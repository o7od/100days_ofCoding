from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def submit_form(forms, submit_button, house_info):
    for i in range(len(forms)):
        forms[i].send_keys(house_info[i])

    submit_button.click()

# 1. Scraping data from zillow website 
zillow_website = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(zillow_website)
soup = BeautifulSoup(response.text, "html.parser")

house_cards = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
all_info = []

# Getting house prices, link and address
for card in house_cards:

    # price, link, address
    price = card.find("span", attrs={"data-test": "property-card-price"}).text.strip("+/mo 1bd")
    link = card.find("a", class_="property-card-link").get("href")
    address = card.find("address", attrs={"data-test": "property-card-addr"}).text.replace("|", "").strip("\n ")

    each_house_info = {
        0: address,
        1: price,
        2: link,
    }

     # add to all_info list
    all_info.append(each_house_info)
   
    
# 2. Filling google form
url = "https://docs.google.com/forms/d/e/1FAIpQLSfLcRbHHdj4Qs-dh7NDSkSAbkDhq_vwDNW4AqCsMP2gX9R1qQ/viewform?usp=publish-editor"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)   
driver = webdriver.Chrome(chrome_options)

# for house_info in all_info:
driver.get(url=url)
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 5)


# filling in google 
for house in all_info:
    forms = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP > input")
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_form(forms, submit_button, house)
    time.sleep(2)
    another_submit = driver.find_element(By.CSS_SELECTOR, ".c2gzEf > a")
    another_submit.click()
    time.sleep(1)
    

