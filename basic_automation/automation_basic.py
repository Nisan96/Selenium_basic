import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def valid_loginTest():
    # step1: Launch Browser
    control = webdriver.Edge()
    control.maximize_window()
    # step2: Get URL
    control.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    # step3: Enter Username
    username_position = control.find_element(By.NAME, "username")
    username_position.send_keys("Admin")
    # step4: Enter password
    password_position = control.find_element(By.NAME, "password")
    password_position.send_keys("admin123")
    # step5: Click Login button
    button_position = control.find_element(By.CLASS_NAME, "orangehrm-login-button")
    button_position.click()
    time.sleep(5)

    control.close()


def invalid_loginTest():
    # step1: Launch Browser
    control = webdriver.Firefox()
    control.maximize_window()
    # step2: Get URL
    control.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    # step3: Enter Username
    username_position = control.find_element(By.NAME, "username")
    username_position.send_keys("sddfdf")
    # step4: Enter password
    password_position = control.find_element(By.NAME, "password")
    password_position.send_keys("adminddgf")
    # step5: Click Login button
    button_position = control.find_element(By.CLASS_NAME, "orangehrm-login-button")
    button_position.click()
    time.sleep(5)

    control.close()


if __name__=="__main__":
    valid_loginTest()
    invalid_loginTest()