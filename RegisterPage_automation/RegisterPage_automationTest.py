import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# Screenshot File Path
screenshot_file_path = "D:\\Automation_testing\\Selenium_basic\\RegisterPage_automation\\screenshots"

def configure_logger(log_filename):
    # Create a new logger for each test
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Create a file handler and set the logging level
    handler = logging.FileHandler(log_filename)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and attach it to the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

def RegisterPage_Valid_Test():
    # Configure Logging settings
    #logging.basicConfig(filename="RegisterPage_Test_Log\\validTest_RegisterPage.log", level=logging.INFO,
                        #format='%(asctime)s - %(levelname)s: %(message)s')

    log1 = configure_logger("RegisterPage_Test_Log\\validTest_RegisterPage.log")

    # step 1: Launch browser
    log1.info("valid RegisterPage Test execution start...")
    control = webdriver.Edge()
    log1.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    log1.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        log1.info("Enter First Name Successfully.")
    else:
        log1.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        log1.info("Enter Last Name Successfully")
    else:
        log1.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        log1.info("Enter E-mail Successfully")
    else:
        log1.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        log1.info("Enter phone number Successfully")
    else:
        log1.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        log1.info("Enter password Successfully")
    else:
        log1.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('UserData_Text_files/valid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[4])
        log1.info("Enter confirm password Successfully")
    else:
        log1.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "Yes"
    subscribe_radio_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.XPATH, "/html//div[@id='content']/form[@action='https://tutorialsninja.com/demo/index.php?route=account/register']//div[@class='form-group']/div[@class='col-sm-10']/label[1]/input[@name='newsletter']")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        #subscribe_radio_button.clear()
        subscribe_radio_button.click()
        log1.info("Subscribe Radio Button clicked Successfully")
        #time.sleep(3)
    else:
        log1.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        #agree_checkbox.clear()
        agree_checkbox.click()
        log1.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        log1.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        log1.info("continue button clicked successfully")
        # time.sleep(5)
    else:
        log1.error("continue button isn't enable...Test Fail")

    # step 21: verify continue button work or not by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/success"
    time.sleep(5)
    actual_url = control.current_url
    if expected_url == actual_url:
        log1.info("Test passed. Register successfully")
        control.get_screenshot_as_file(screenshot_file_path + "\\RegisterPage_ValidTest_passed.png")
    else:
        log1.info("Test failed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\RegisterPassed_ValidTest_failed.png")

    control.quit()

def RegisterPage_Invalid_Test():
    # Configure Logging settings
    #logging.basicConfig(filename="RegisterPage_Test_Log\\invalidTest_RegisterPage.log", level=logging.INFO,
                        #format='%(asctime)s - %(levelname)s: %(message)s')

    logger = configure_logger("RegisterPage_Test_Log\\invalidTest_RegisterPage.log")

    # step 1: Launch browser
    logger.info("Invalid RegisterPage Test execution start...")
    control = webdriver.Edge()
    logger.info("Edge launch successfully")
    control.maximize_window()
    control.implicitly_wait(10)

    # step 2: Open URL
    control.get("https://tutorialsninja.com/demo/index.php?route=account/register")
    control.implicitly_wait(10)
    logger.info("Register page open Successful.")

    # step 3: Find location of First Name
    firstName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-firstname")))
    firstName_field_enable_state = firstName_field.is_enabled()
    print("firstName_field is enable:", firstName_field_enable_state)

    # step 4: verify First Name field is enabled or not and enter First Name
    if firstName_field_enable_state == True:
        firstName_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        firstName_field.send_keys(content[0])

        logger.info("Enter First Name Successfully.")
    else:
        logger.error("First name field isn't enable.....Test Fail")

    # step 5: Find location of Last Name
    lastName_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-lastname")))
    lastName_field_enable_state = lastName_field.is_enabled()
    print("lastName_field is enable:", lastName_field_enable_state)

    # step 6: verify Last Name field is enabled or not and enter Last Name
    if lastName_field_enable_state == True:
        lastName_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        lastName_field.send_keys(content[1])
        logger.info("Enter Last Name Successfully")
    else:
        logger.error("Last Name field isn't enable....Test fail")

    # step 7: Find location of E-Mail
    email_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-email")))
    email_field_enable_state = email_field.is_enabled()
    print("email_field is enable:", email_field_enable_state)

    # step 8: verify E-Mail field is enabled or not and enter E-Mail
    if email_field_enable_state == True:
        email_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        email_field.send_keys(content[2])
        logger.info("Enter E-mail Successfully")
    else:
        logger.error("email field isn't enable....Test fail")

    # step 9: Find location of Telephone
    telephone_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-telephone")))
    telephone_field_enable_state = telephone_field.is_enabled()
    print("telephone_field is enable:", telephone_field_enable_state)

    # step 10: verify Telephone field is enabled or not and enter Telephone
    if telephone_field_enable_state == True:
        telephone_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        telephone_field.send_keys(content[3])
        logger.info("Enter phone number Successfully")
    else:
        logger.error("telephone field isn't enable....Test fail")

    # step 11: Find location of Password
    password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-password")))
    password_field_enable_state = password_field.is_enabled()
    print("password_field is enable:", password_field_enable_state)

    # step 12: verify Password field is enabled or not and enter Password
    if password_field_enable_state == True:
        password_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        password_field.send_keys(content[4])
        logger.info("Enter password Successfully")
    else:
        logger.error("password field isn't enable....Test fail")

    # step 13: Find location of Password Confirm
    confirm_password_field = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.ID, "input-confirm")))
    confirm_password_field_enable_state = confirm_password_field.is_enabled()
    print("confirm_password_field is enable:", confirm_password_field_enable_state)

    # step 14: verify Password Confirm field is enabled or not and enter Password Confirm
    if confirm_password_field_enable_state == True:
        confirm_password_field.clear()
        with open('UserData_Text_files/invalid_RegisterPage_test.txt', 'r') as f:
            content = f.readlines()
            f.close()
        confirm_password_field.send_keys(content[5])
        logger.info("Enter confirm password Successfully")
    else:
        logger.error("Password Confirm field isn't enable....Test fail")

    # Find location of newsletter subscribe button "NO"
    subscribe_radio_button = WebDriverWait(control, 5).until(
        ec.visibility_of_element_located((By.XPATH, "/html//div[@id='content']/form[@action='https://tutorialsninja.com/demo/index.php?route=account/register']//div[@class='form-group']/div[@class='col-sm-10']/label[2]/input[@name='newsletter']")))
    subscribe_radio_button_enable_state = subscribe_radio_button.is_enabled()
    print("subscribe_radio_button is enable:", subscribe_radio_button_enable_state)

    # step 16: verify Newsletter Subscribe Radio Button "Yes" is enabled or not and click on this
    if subscribe_radio_button_enable_state == True:
        #subscribe_radio_button.clear()
        subscribe_radio_button.click()
        logger.info("Subscribe Radio Button clicked Successfully")
        # time.sleep(3)
    else:
        logger.error("Subscribe Radio Button isn't enable....Test fail")

    # step 17: Find location of agree policy checkbox
    agree_checkbox = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.NAME, "agree")))
    agree_checkbox_enable_state = agree_checkbox.is_enabled()
    print("agree police checkbox is enable:", agree_checkbox_enable_state)

    # step 18: verify agree policy checkbox is enabled or not and click on this
    if agree_checkbox_enable_state == True:
        #agree_checkbox.clear()
        agree_checkbox.click()
        logger.info("agree checkbox checked Successfully")
        time.sleep(3)
    else:
        logger.error("agree checkbox isn't enable....Test fail")

    # step 19: Find location of continue button
    continue_button = WebDriverWait(control, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
    continue_button_enable_state = continue_button.is_enabled()
    print("continue_button_enable_state is enable:", continue_button_enable_state)

    # step 20: verify continue button is enabled or not and click on this
    if continue_button_enable_state == True:
        continue_button.click()
        logger.info("continue button clicked successfully")
        # time.sleep(5)
    else:
        logger.error("continue button isn't enable...Test Fail")

    # step 21: verify continue button work or not by checking url
    expected_url = "https://tutorialsninja.com/demo/index.php?route=account/register"
    time.sleep(3)
    actual_url = control.current_url
    if expected_url == actual_url:
        logger.info("Test passed. Can't Register")
        control.get_screenshot_as_file(screenshot_file_path + "\\RegisterPage_InvalidTest_passed.png")
    else:
        logger.info("Test failed. Account Created")
        control.get_screenshot_as_file(screenshot_file_path + "\\RegisterPassed_InvalidTest_failed.png")

    control.quit()


# Main Function

if __name__=="__main__":
    RegisterPage_Valid_Test()
    RegisterPage_Invalid_Test()
