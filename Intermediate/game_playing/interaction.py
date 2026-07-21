from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keeping browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Instantiating our chrome broswer driver
driver = webdriver.Chrome(chrome_options)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
driver.implicitly_wait(1)


first_name = driver.find_element(By.NAME, "fName")
second_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
button = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("Ozodbek")
second_name.send_keys("Otamirzayev")
email.send_keys("ozodotamirzayev@gmail.com")


button.send_keys(Keys.RETURN)





# articles = driver.find_element(By.ID, "mwDw")
# articles.click()

# portals = driver.find_element(By.LINK_TEXT, "Content portals")
# portals.click()


#Locating input box
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python", Keys.RETURN)

# driver.quit()