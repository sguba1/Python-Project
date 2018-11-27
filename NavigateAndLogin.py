import CommonFunctions
import time

from selenium import webdriver

def LoginApp():
    Username = "Admin"
    Password = "admin123"

    driver = webdriver.Chrome("C:\\Users\\sachi\\Downloads\\chromedriver_win32\\chromedriver.exe")

    driver.get("https://opensource-demo.orangehrmlive.com/")

    usernameField = driver.find_element_by_id("txtUsername")
    CommonFunctions.clickElement(usernameField)
    usernameField.send_keys(Username)
    time.sleep(1)

    passwordField = driver.find_element_by_id("txtPassword")
    CommonFunctions.highlight(passwordField)
    passwordField.send_keys(Password)
    time.sleep(1)

    loginButton = driver.find_element_by_id("btnLogin")
    CommonFunctions.highlight(loginButton)
    CommonFunctions.clickElement(loginButton)

    return driver

# LoginApp()