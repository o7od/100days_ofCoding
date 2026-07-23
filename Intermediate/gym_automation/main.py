from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os

######################## Gym Credentials ########################
EMAIL = "ozodotamirzaev06@gmail.com"
PASSWORD = "o2od0615@"
GYM_URL = "https://appbrewery.github.io/gym/"

# This will retry any function  
def retry(func, retries=1):
    if not func() and retries <= 7:
        retries += 1
        print(f"Trying {func}. Attempt: {retries}")

#--------------------------- SETUP --------------------------#
# To keep the window open 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# This will give selenium to store user's profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(chrome_options)

driver.implicitly_wait(10)
driver.get(GYM_URL)
driver.maximize_window()
#-----------------------------------------LOGIN -------------------------------------------------#
wait = WebDriverWait(driver, 2)
def login():
    try:
        # Locating the login button as soon as it is visible on the page
        login_button = wait.until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )
        login_button.click()
        driver.execute_script("window.scrollBy(0, 100)")
        email_entry = wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        # Fill in login form
        email_entry.clear()
        email_entry.send_keys(EMAIL)
        password_entry = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_entry.clear()
        password_entry.send_keys(PASSWORD)

        # Click Log in 
        submit_button = wait.until(
            EC.presence_of_element_located((By.ID, "submit-button"))
        )
        submit_button.click()
    except Exception as e:
        # print("Element not found or Timed out: ", e)
        retry(login)
        return False

# We test if after clicking the login button, we are on the schedule page, if not we try clicking again
try:
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
except TimeoutException:
    print(True)
    retry(login)
else:
    print("Successful Login")
#----------------------------------- Decide Days for booking  ----------------------------------#
gym_days = ["Tuesday", "Thursday"]
gym_short_days = [day[0:3] for day in gym_days]
booked_classes = []
waitlisted_classes = []
already_booked_waitlisted = 0
def book_class(already_booked):
    #----------------------------------- Selecting Classes ----------------------------------#
    schedules = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

    for day in gym_short_days:
        for schedule in schedules:
            day_group = schedule.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
            day_title = day_group.find_element(By.TAG_NAME, "h2").text

            if day in day_title:
                class_time = schedule.find_element(By.CSS_SELECTOR, "p[id^='class-time']").text
                if "6:00 PM" in class_time:
                    # Class Name
                    class_name = schedule.find_element(By.CSS_SELECTOR, "h3[id^='class-name']").text
                    
                    # Button
                    # We wait until the button is clickable 
                    book_button = driver.find_element(By.CSS_SELECTOR, "button[id^='book-button']")
                    # book_button = wait.until(EC.element_to_be_clickable(()))
                    # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", book_button)

                    # Joined Waitlist 
                    if book_button.text == "Join Waitlist":
                        book_button.click()
                        print(f"✔ Joined waitlist for: {class_name} on {day_title} at {class_time}")
                        waitlisted_classes.append({"class": class_name, "class_time": day_title})
                    elif book_button.text == "Booked": 
                        print(f"✔ Already booked: {class_name} on {day_title} at {class_time}")
                        already_booked += 1
                        return already_booked
                    elif book_button.text == "Waitlisted":
                        print(f"Already on a waitlist: {class_name} on {day_title}")
                        already_booked += 1
                        return already_booked
                    else:
                        book_button.click()
                        print(f"✔ Successfully Booked: {class_name} on {day_title} at {class_time}")
                        booked_classes.append({"class": class_name, "class_time": day_title})
                        
                    break
                    

#----------------------------------- Printing Summary ----------------------------------#
result = book_class(already_booked_waitlisted)
already_booked_waitlisted = 0 if result is None else result


print("--------- BOOKING SUMMARY ---------")
print(f"New Bookings: {len(booked_classes)}\n"
      f"New waitlists entries: {len(waitlisted_classes)}\n"
      f"Already booked/waitlisted: {already_booked_waitlisted}\n"
      f"Total {gym_days[0]} & {gym_days[1]} 6pm classes: {len(booked_classes) + len(waitlisted_classes) + already_booked_waitlisted}")


# print("--------- DETAILED CLASS LIST  ---------")
# for i in range(len(booked_classes)):
#     print(f" • [New Booking] {booked_classes[i].get("class")} on ({booked_classes[i].get("class_time")})")
# for j in range(len(waitlisted_classes)):
#     print(f" • [New Waitlist] {waitlisted_classes[j].get("class")} on ({waitlisted_classes[j].get("class_time")})")

#----------------------------------- Verifying bookings ----------------------------------#
def get_my_bookings():
    my_bookings_page = driver.find_element(By.ID, "my-bookings-link")
    my_bookings_page.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "MyBookings_pageTitle__i0Jkj")))

    # bookings = driver.find_element(By.CLASS_NAME, "MyBookings_pageTitle__i0Jkj")
    # Get booked classes card
    all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
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
            pass

    print("-------- Verification Result -------")
    expected_num = len(booked_classes) + len(waitlisted_classes) + already_booked_waitlisted
    difference = expected_num - verified_count

    print(f"Expected: {expected_num} bookings\nFound: {verified_count} bookings")
    if difference == 0:
        print(f"✅ SUCCESS: All bookings verified")
    else: 
        print(f"❌ MISMATCH: Missing {difference} bookings")

get_my_bookings()       
# driver.quit()