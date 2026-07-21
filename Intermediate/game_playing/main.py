from selenium import webdriver 
from selenium.webdriver.common.by import By

# Keep Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(chrome_options)
driver.get("https://www.python.org/")

driver.implicitly_wait(1)

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.tag_name)
# button = driver.find_element(by=By.ID, value="submit")
# print(button.get_attribute("title"))
# anchor_tag = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(anchor_tag.get_attribute("href"))
# success_story = driver.find_element(by=By.XPATH, value='//*[@id="container"]/li[5]/ul/li[6]/a')
# link = success_story.get_attribute("href")
# print(success_story.text)
# another_driver = webdriver.Chrome(chrome_options)
# another_driver.get(f"{link}")

########### CHALLENGE ###########
upcoming_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu li time")
upcoming_events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget .menu li a")

event_history = {}
for i in range(len(upcoming_dates)):
    event_history[i] = {
        "Event": upcoming_events[i].text,
        "Date": upcoming_dates[i].text,
    }

print(event_history)


driver.quit()



