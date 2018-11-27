import CommonFunctions
import NavigateAndLogin
import Logout
import openpyxl
from openpyxl.styles import Font

def extractUsersInfo():

    driver = NavigateAndLogin.LoginApp()

    wk = openpyxl.Workbook()
    sh = wk.active
    sh.title = "User Information"
    sh['A1'] = 'Username'
    sh['A1'].font = Font(bold=True)
    sh['B1'] = 'User Role'
    sh['B1'].font = Font(bold=True)
    sh['C1'] = 'Employee Name'
    sh['C1'].font = Font(bold=True)
    sh['D1'] = 'Status'
    sh['D1'].font = Font(bold=True)


    admin_menu = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
    CommonFunctions.clickElement(admin_menu)

    row_count = len(driver.find_elements_by_xpath("//*[@id='resultTable']/tbody/tr"))
    print(row_count)
    for i in range(1, row_count+1):
        username_column = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+ str(i) +"]/td[2]/a")
        username = username_column.text
        print(username)
        sh['A'+str(i+1)].value = username

    for j in range(1,row_count+1):
        user_role_column = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+ str(j) +"]/td[3]")
        user_role = user_role_column.text
        print(user_role)
        sh['B'+str(j+1)].value = user_role

    for k in range(1,row_count+1):
        employee_name_column = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+ str(k) +"]/td[4]")
        employee_name = employee_name_column.text
        print(employee_name)
        sh['C'+str(k+1)].value = employee_name

    for l in range(1,row_count+1):
        status_column = driver.find_element_by_xpath("//*[@id='resultTable']/tbody/tr["+ str(l) +"]/td[5]")
        status = status_column.text
        print(status)
        sh['D'+ str(l+1)].value = status

    driver.execute_script("window.scrollTo(0, 500)")
    driver.get_screenshot_as_file('C:\\Users\\sachi\\Downloads\\Screenshot.png')
    wk.save("C:\\Users\\sachi\\Downloads\\Script Programming - Python\\User Info.xlsx")

    Logout.logout(driver)
extractUsersInfo()