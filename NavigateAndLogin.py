import CommonFunctions
import time

from selenium import webdriver

def LoginApp():
    # Define the log in user name and password
    Username = "Admin"
    Password = "admin123"

    #Use driver to open file chromedriver.exe
    driver = webdriver.Chrome("C:\\Users\\ShiyuF\\Python36\\chromedriver.exe")

    #Open the website
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()

    #Input user name
    usernameField = driver.find_element_by_id("txtUsername")
    CommonFunctions.clickElement(usernameField)
    usernameField.send_keys(Username)
    time.sleep(1)

    #Input password
    passwordField = driver.find_element_by_id("txtPassword")
    CommonFunctions.highlight(passwordField)
    passwordField.send_keys(Password)
    time.sleep(1)

    #Click log in button
    loginButton = driver.find_element_by_id("btnLogin")
    CommonFunctions.highlight(loginButton)
    CommonFunctions.clickElement(loginButton)

    return driver

#LoginApp()
