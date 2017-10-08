#!/usr/bin/python
# -*- coding: utf-8 -*-

from PageObject_AboutUs import *
from PageObject_Admin import *
from PageObject_Home import *
from PageObject_Registration import *
from selenium import webdriver
from utilities_custom_usage import *

chrome_driver_path_used = 'D:\Automation_project\Commom_jars_files\Selenium_Chromedriver_win32\chromedriver.exe'
delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec


class HandleClassImpl:
    def __init__(self):
        pass

    def perform_initial_setup(self, global_list_variables):
        print ('Performing initial set up, invoking browser')
        global_list_variables.append(webdriver.Chrome(executable_path=chrome_driver_path_used))
        global_list_variables[0].maximize_window()
        global_list_variables.append('success')
        return True

    def perform_some_action_on_home_page(self, global_list_variables, url_home_page):
        print ('Performing some action on home page')
        chrome_web_driver = global_list_variables[0]
        home_page = HomePage(chrome_web_driver)
        home_page.method_home_page_launch_home_url(chrome_web_driver, url_home_page)
        home_page.method_home_page_login(chrome_web_driver,)
        home_page.method_home_page_navigate_to_about_us(chrome_web_driver,)
        global_list_variables.append('success')
        return

    def perform_some_action_on_about_us_page(self, global_list_variables,):
        print ('Performing some action on about us page')
        chrome_web_driver = global_list_variables[0]
        about_us_page = AboutUsPage(chrome_web_driver)
        about_us_page.method_verify_specific_message(chrome_web_driver, 'not', 'a real bank')
        about_us_page.method_about_us_navigate_to_admin(chrome_web_driver,)
        global_list_variables.append('success')
        return

    def perform_some_action_on_admin_page(self, global_list_variables,):
        print ('Performing some action on admin page')
        chrome_web_driver = global_list_variables[0]
        admin_page = AdminPage(chrome_web_driver)
        admin_page.method_admin_page_clean_database(chrome_web_driver,)
        admin_page.method_admin_page_initialize_database(chrome_web_driver,)
        admin_page.method_home_page_navigate_to_register(chrome_web_driver,)
        global_list_variables.append('success')
        return

    def perform_some_action_on_registration_page(self, global_list_variables,):
        print ('Performing some action on registration page')
        chrome_web_driver = global_list_variables[0]
        registration_page = RegistrationPage(chrome_web_driver)
        registration_page.method_registration_page_clean_database(chrome_web_driver)
        global_list_variables.append('success')
        return

    def final_verification(self, global_list_variables,):
        print ('Performing final verification for each step pass or fail')
        chrome_web_driver = global_list_variables[0]
        chrome_web_driver.close()
        chrome_web_driver.quit()
        compare_success = UtilitiesCustom()
        compare_success.method_utilities_compare_all_success_failure(global_list_variables)
        return


obj_handle_impl = HandleClassImpl()
