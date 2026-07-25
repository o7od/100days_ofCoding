from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


start = time.time()

time.sleep(5)

end = time.time()
passed_time = int(end - start)

# Setup Chrome Driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)
driver.maximize_window()

#Selecting a language
try:
    select_language = driver.find_element(By.ID, 'langSelect-EN')
    select_language.click()
    # select_language.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
except NoSuchElementException:
    print("No language selection found")


# Getting all the products
products = [driver.find_element(By.ID, f"product{i}") for i in range (10)]

# Scrolling to the products shop
element = driver.find_element(By.ID, "sectionRight")
driver.execute_script("arguments[0].scrollTop += 250;", element)

cookies_amount = driver.find_element(By.ID, "cookies")
print(cookies_amount.text.split("\n"))

# Start Clicking 
start_time = time.time()
game_time = time.time()
time_out = 5
while True:
    time.sleep(0.1)
    button_big_cookie = driver.find_element(By.ID, "bigCookie")
    button_big_cookie.click()

    # Checks every 'time_out' seconds to buy boosters
    if time.time() - start_time >= time_out:
        print("5 seconds has passed")
        for product in reversed(products):
            if "enabled" in product.get_attribute("class"):
                product.click()
                time_out += 1

        start_time = time.time()

        
    # Checks if the game time ended
    if time.time() - game_time >= 60:
        cookies_amount = driver.find_element(By.ID, "cookies")
        # cookies_per_second = driver.find_element(By.ID, "cookiesPerSecond")
        result = cookies_amount.text.split("\n")
        print(f"1 Minute Passed\nHere is the total number of cookies clicked: {result[0]}\nPer second cookie rate is {result[1]}")
        driver.quit()
        break