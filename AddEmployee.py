import NavigateAndLogin
import CommonFunctions
import os
import time

def addEmployee():

    driver = NavigateAndLogin.LoginApp()

    # Click on PIM Module
    pim_module = driver.find_element_by_id("menu_pim_viewPimModule")
    CommonFunctions.clickElement(pim_module)

    # Click on Add Employee Button
    add_employee = driver.find_element_by_id("menu_pim_addEmployee")
    CommonFunctions.clickElement(add_employee)

    # Enter First Name in FirstName Field
    firstname_field = driver.find_element_by_id("firstName")
    CommonFunctions.clickElement(firstname_field)
    firstname_field.send_keys("Sample")

    # Enter Last Name in LastName Field
    lastname_field = driver.find_element_by_id("lastName")
    CommonFunctions.clickElement(lastname_field)
    lastname_field.send_keys("User")

    # Enter Employee ID
    employeeid_field = driver.find_element_by_id("employeeId")
    CommonFunctions.clickElement(employeeid_field)
    employeeid_field.send_keys("007")

    # Upload Image
    browse_button = driver.find_element_by_id("photofile")
    CommonFunctions.clickElement(browse_button)
    os.system(r"C:\\Users\\ShiyuF\\Desktop\\upfile.exe")

    employeesave_button = driver.find_element_by_id("btnSave")
    CommonFunctions.clickElement(employeesave_button)

    time.sleep(10)

addEmployee()