from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#captive portal URL
portal_url = "https://planetcampus.wifirst.net/sessions/new"

# user creditentials
username = "your email address goes here"
password = "and you password goes here"

# firefox webdriver
driver = webdriver.Firefox()

try:
    driver.get(portal_url)

    # waiting in case of low network speed
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))  # updated selector,may break one day
    )

    # filing the field username with user cred.
    email_field.send_keys(username)

    # same but for passwrd
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)

    # then i submit the form
    password_field.send_keys(Keys.RETURN)

    # then waiting before check
    time.sleep(5)

    # checking if it worked, finger crossed lmao
    if "success" in driver.page_source:  
        print("Authentification réussie.")
    else:
        print("Échec de l'authentification.")

finally:
    # closing the shit this code is
    driver.quit()
