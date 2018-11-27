import CommonFunctions
import NavigateAndLogin
import Logout
from selenium import webdriver
import time

def verifyModulesStartPage():

    driver = NavigateAndLogin.LoginApp()

    admin = 'Admin'
    pim = 'PIM'
    leave = 'Leave'
    time = 'Time'
    recruitment = 'Recruitment'
    performance = 'Performance'
    dashboard = 'Dashboard'
    directory = 'Directory'

    admin_menu = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
    CommonFunctions.highlight(admin_menu)
    assert admin_menu.text == admin

    pim_menu = driver.find_element_by_id("menu_pim_viewPimModule")
    CommonFunctions.highlight(pim_menu)
    assert pim_menu.text == pim

    leave_menu = driver.find_element_by_id("menu_leave_viewLeaveModule")
    CommonFunctions.highlight(leave_menu)
    assert leave_menu.text == leave

    time_menu = driver.find_element_by_id("menu_time_viewTimeModule")
    CommonFunctions.highlight(time_menu)
    assert time_menu.text == time

    recruitment_menu = driver.find_element_by_id("menu_recruitment_viewRecruitmentModule")
    CommonFunctions.highlight(recruitment_menu)
    assert recruitment_menu.text == recruitment

    performance_menu = driver.find_element_by_id("menu__Performance")
    CommonFunctions.highlight(performance_menu)
    assert  performance_menu.text == performance

    dashboard_menu = driver.find_element_by_id("menu_dashboard_index")
    CommonFunctions.highlight(dashboard_menu)
    assert dashboard_menu.text == dashboard

    directory_menu = driver.find_element_by_id("menu_directory_viewDirectory")
    CommonFunctions.highlight(directory_menu)
    assert directory_menu.text == directory

    print("Verified the Menu's present in Home Page")

    Logout.logout(driver)

verifyModulesStartPage()