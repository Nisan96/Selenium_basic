import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def loginTest_valid():
    # step1: Launch browser
    driver = webdriver.Firefox()
    driver.maximize_window()

    # step2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # step3: Enter username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("Admin")

    # step4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")

    # step5: Click Login button
    login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
    login_button.click()
    time.sleep(5)

    driver.close()


def loginTest_invalid():
    #step1: Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    #step2: Open URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)

    # step3: Enter username
    username_field = driver.find_element(By.NAME, "username")
    username_field.send_keys("ddffg")

    # step4: Enter Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin23435")

    # step5: Click Login button
    login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button")
    login_button.click()
    time.sleep(3)

    driver.close()

if __name__ == "__main__":

    loginTest_valid()
    loginTest_invalid()