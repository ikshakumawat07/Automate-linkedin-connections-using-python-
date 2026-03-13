from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

print("LinkedIn Auto Connection Bot")

# ask user how many connections to send
limit = int(input("How many connection requests do you want to send? "))

options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# open linkedin search page
driver.get("https://www.linkedin.com/search/results/people/?keywords=python%20developer")

time.sleep(3)

# refresh page automatically
driver.refresh()

time.sleep(5)

sent = 0

while sent < limit:

    connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[text()='Connect']]")

    # randomize order so different people are selected
    random.shuffle(connect_buttons)

    for button in connect_buttons:

        if sent >= limit:
            break

        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            time.sleep(1)

            driver.execute_script("arguments[0].click();", button)

            send_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Send without a note']]"))
            )

            driver.execute_script("arguments[0].click();", send_button)

            sent += 1

            print(f"Connection sent: {sent}/{limit}")

            time.sleep(random.randint(5,9))

        except:
            print("Skipped profile")

    # scroll to load more profiles
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

print("Finished sending connection requests")
