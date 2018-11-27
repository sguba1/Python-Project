
import CommonFunctions
import time

def logout(self):

    #driver = webdriver.Chrome("C:\\Users\\sachi\\Downloads\\chromedriver_win32\\chromedriver.exe")

    dashboardModule = self.find_element_by_id("menu_dashboard_index")
    CommonFunctions.clickElement(dashboardModule)

    welcomeAdmin_button = self.find_element_by_id("welcome")
    CommonFunctions.clickElement(welcomeAdmin_button)

    logoutButton = self.find_element_by_xpath("//*[@id='welcome-menu']/ul/li[2]/a")
    CommonFunctions.clickElement(logoutButton)

    time.sleep(3)
    self.close()

