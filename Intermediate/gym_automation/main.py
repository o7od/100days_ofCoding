from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time
import os
from dotenv import load_dotenv
load_dotenv()



# This will retry any function  
def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt {i+1}")
        try:
            return func() # this will raise TimeOutException if the schedule-page doesn't appear within 2 seconds or ElementClickInterceptedException
        except TimeoutException:
            if i == retries-1:
                raise
            time.sleep(1)
        except ElementClickInterceptedException:
            print("Element click intercepted")
            if i == retries-1:
                raise
            time.sleep(1)

# This function handles the entire login process
def login():
    # Locating the login button as soon as it is visible on the page
    login_button = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    login_button.click()

    # Fill in login form
    email_entry = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_entry.clear()
    email_entry.send_keys(os.environ.get("EMAIL"))

    password_entry = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password_entry.clear()
    password_entry.send_keys(os.environ.get("PASSWORD"))

    # Click Log in 
    submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

#----------------------------------- Selecting Classes ----------------------------------#
# This function handles everything related to booking a class
def book_class():
    schedules = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for schedule in schedules:
        day_group = schedule.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
        day_title = day_group.find_element(By.TAG_NAME, "h2").text
        print(day_title)

        if "Thu" in day_title or "Tue" in day_title:
            class_time = schedule.find_element(By.CSS_SELECTOR, "p[id^='class-time']").text
            if "6:00 PM" in class_time:
                # Class Name
                class_name = schedule.find_element(By.CSS_SELECTOR, "h3[id^='class-name']").text
                print(class_name)
                
                # Button
                # book_button = wait.until(EC.element_to_be_clickable(()))
                book_button = schedule.find_element(By.CSS_SELECTOR, "button[id^='book-button']")

                # Joined Waitlist 
                if book_button.text == "Join Waitlist":
                    while book_button.is_enabled():
                        print(book_button.is_enabled())
                        book_button.click()
                        time.sleep(2)
                    print(f"✔ Joined waitlist for: {class_name} on {day_title} at {class_time}")
                    waitlisted_classes.append({"class": class_name, "class_time": day_title})
                elif book_button.text == "Booked": 
                    print(f"✔ Already booked: {class_name} on {day_title} at {class_time}")
                    global already_booked_waitlisted
                    already_booked_waitlisted += 1
                    return already_booked_waitlisted
                elif book_button.text == "Waitlisted":
                    print(f"Already on a waitlist: {class_name} on {day_title}")
                    already_booked_waitlisted += 1
                    return already_booked_waitlisted
                else:
                    while book_button.is_enabled():
                        print(book_button.is_enabled())
                        book_button.click()
                        time.sleep(2)
                    print(f"✔ Successfully Booked: {class_name} on {day_title} at {class_time}")
                    booked_classes.append({"class": class_name, "class_time": day_title})

# #----------------------------------- Verifying bookings ----------------------------------#
def get_my_bookings():
    my_bookings_page = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_page.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "MyBookings_pageTitle__i0Jkj")))

    # Get booked classes card
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    if not all_cards:
        raise TimeoutException("No Booking cards found - page may have not loaded")
    return all_cards
    


#--------------------------- SETUP --------------------------#
def set_up():
    # To keep the window open 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    # This will give selenium to store user's profile
    user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    driver = webdriver.Chrome(chrome_options)

    driver.implicitly_wait(10)
    driver.get(os.environ.get("GYM_URL"))
    driver.maximize_window()
    return driver

#-----------------------------------------LOGIN -------------------------------------------------#
driver = set_up()
wait = WebDriverWait(driver, 2)
retry(func=login, description="login")
#----------------------------------- Decide Days for booking  ----------------------------------#
gym_days = ["Tuesday", "Thursday"]
gym_short_days = [day[0:3] for day in gym_days]
booked_classes = []
waitlisted_classes = []
already_booked_waitlisted = 0
retry(func=book_class, description="booking a class")

#----------------------------------- Printing Summary ----------------------------------#
print("--------- BOOKING SUMMARY ---------")
print(f"New Bookings: {len(booked_classes)}\n"
      f"New waitlists entries: {len(waitlisted_classes)}\n"
      f"Already booked/waitlisted: {already_booked_waitlisted}\n"
      f"Total {gym_days[0]} & {gym_days[1]} 6pm classes: {len(booked_classes) + len(waitlisted_classes) + already_booked_waitlisted}")


print("--------- DETAILED CLASS LIST  ---------")
for i in range(len(booked_classes)):
    print(f" • [New Booking] {booked_classes[i].get("class")} on ({booked_classes[i].get("class_time")})")
for j in range(len(waitlisted_classes)):
    print(f" • [New Waitlist] {waitlisted_classes[j].get("class")} on ({waitlisted_classes[j].get("class_time")})")


all_cards = retry(func=get_my_bookings, description="Getting my Bookings")
verified_count = 0
print("-------- Verifying on My Bookings Page --------")
for card in all_cards:
    try:
        when_text = card.find_element(By.XPATH, ".//p[strong[text()='When:']]").text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            name_class = card.find_element(By.TAG_NAME, "h3").text
            print(f"✔ Verified: {name_class}")
            verified_count += 1
    except NoSuchElementException:
        # if no when_text element found
        pass

print("-------- Verification Result -------")
expected_num = len(booked_classes) + len(waitlisted_classes) + already_booked_waitlisted
difference = expected_num - verified_count

print(f"Expected: {expected_num} bookings\nFound: {verified_count} bookings")
if difference == 0:
    print(f"✅ SUCCESS: All bookings verified")
else: 
    print(f"❌ MISMATCH: Missing {difference} bookings")

