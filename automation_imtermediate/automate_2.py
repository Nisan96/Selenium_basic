import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#configure logging settings
logging.basicConfig(filename="test_log.log",level=logging.INFO,format= '%(asctime)s - %(levelname)s: %(message)s')
screenshot_file_path = "D:\\Automation_testing\\Selenium_basic\\automation_imtermediate\\screenshot"

def valid_loginTest():
    # step1: Launch browser
    logging.info("valid loginTest execution start...")
    control = webdriver.Edge()
    logging.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(5)

    # step2: Open URL
    control.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    control.implicitly_wait(10)
    logging.info("Login page open Successful.")

    # step3: find location of username
    Username_field = WebDriverWait(control,5).until(ec.visibility_of_element_located((By.NAME,"username")))
    Username_field_enable_state = Username_field.is_enabled()
    print("Username_field_enable_state is enable:", Username_field_enable_state)

    # step4: verify username field is enabled or not and enter username
    if Username_field_enable_state == True:
        Username_field.clear()
        Username_field.send_keys("Admin")
        logging.info("Type Username sucessfully")
    else:
        logging.error("Username field is not enable...Test Fail")

    # step5: find location of password
    Password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "password")))
    Password_field_enable_state = Password_field.is_enabled()
    print("Username_field_enable_state is enable:", Password_field_enable_state)

    # step6: verify password field is enabled or not and enter password
    if Password_field_enable_state == True:
        Password_field.clear()
        Password_field.send_keys("admin123")
        logging.info("Enter Password sucessfully")
    else:
        logging.error("Password field is not enable...Test Fail")

    # step7: click login button
    Login_button = WebDriverWait(control,5).until(ec.visibility_of_element_located((By.CLASS_NAME,"orangehrm-login-button")))
    Login_button_enable_state = Login_button.is_enabled()
    print("Login_button_enable_state is enable:", Login_button_enable_state)
    if Login_button_enable_state == True:
        Login_button.click()
        logging.info("Login button clicked successfully")
        time.sleep(5)
    else:
        logging.error("Login button doesn't work...Test Fail")

    # step8: verify login button work or not by checking url
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    actual_url = control.current_url
    if expected_url == actual_url:
        logging.info("Test passed. Login successfully")
        control.get_screenshot_as_file(screenshot_file_path+"\\login_ValidTest_passed.png")
    else:
        logging.info("Test failed. Can't login")
        control.get_screenshot_as_file(screenshot_file_path + "\\login_ValidTest_failed.png")

    control.close()
    logging.info('Valid Login Test execution completed..')



def invalid_loginTest():
    # step1: Launch browser
    logging.info("Invalid loginTest execution start...")
    control = webdriver.Firefox()
    logging.info("Firefox launch successfully")
    control.maximize_window()
    control.implicitly_wait(5)

    # step2: Open URL
    control.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    control.implicitly_wait(15)
    logging.info("Login page open Successful.")

    # step3: find location of username
    Username_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "username")))
    Username_field_enable_state = Username_field.is_enabled()
    print("Username_field_enable_state is enable:", Username_field_enable_state)

    # step4: verify username field is enabled or not and enter username
    if Username_field_enable_state == True:
        Username_field.clear()
        Username_field.send_keys("asghjk")
        logging.info("Type Username sucessfully")
    else:
        logging.error("Username field is not enable...Test Fail")

    # step5: find location of password
    Password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "password")))
    Password_field_enable_state = Password_field.is_enabled()
    print("Username_field_enable_state is enable:", Password_field_enable_state)

    # step6: verify password field is enabled or not and enter password
    if Password_field_enable_state == True:
        Password_field.clear()
        Password_field.send_keys("123dghh")
        logging.info("Enter Password sucessfully")
    else:
        logging.error("Password field is not enable...Test Fail")

    # step7: click login button
    Login_button = WebDriverWait(control, 5).until(
        ec.visibility_of_element_located((By.CLASS_NAME, "orangehrm-login-button")))
    Login_button_enable_state = Login_button.is_enabled()
    print("Login_button_enable_state is enable:", Login_button_enable_state)
    if Login_button_enable_state == True:
        Login_button.click()
        logging.info("Login button clicked successfully")
        time.sleep(5)
    else:
        logging.error("Login button doesn't work...Test Fail")

    # step8: verify login button work or not by checking url
    actual_error = control.find_element(By.CLASS_NAME,"oxd-alert-content-text").text
    actual_error_message = actual_error
    print("actual error message:", actual_error)
    expected_error_message = "Invalid credentials"
    if expected_error_message == actual_error_message:
        logging.info("Test passed. Login failed.Error message: " + actual_error_message)
        # capture snapshot
        control.get_screenshot_as_file(screenshot_file_path + "\\login_InvalidTest_passed.png")
    else:
        logging.info("Test failed. Did not get expected error message: " + expected_error_message)
        # capture snapshot
        control.get_screenshot_as_file(screenshot_file_path + "\\login_InvalidTest_failed.png")

    control.close()
    logging.info('Invalid Login Test execution completed..')





if __name__=="__main__":
    valid_loginTest()
    #invalid_loginTest()