#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from page_objects import PageObject, PageElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

delay_min = 3 # sec
delay_medium = 5 # sec
delay_max = 9 # sec


class AdminPage(PageObject):
    link_register = PageElement(css = "a[href='register.htm']")
    button_database_clean = PageElement(css="button[value='CLEAN']")
    button_database_initialize = PageElement(css="button[value='INIT']")
    action_result_message = PageElement(xpath='//*[@id="rightPanel"]/p/b')

    def method_admin_page_clean_database(self, current_web_driver,):
        self.button_database_clean.click()
        WebDriverWait(current_web_driver,delay_min).until(expected_conditions.visibility_of(self.action_result_message))
        return

    def method_admin_page_initialize_database(self, current_web_driver,):
        self.button_database_initialize.click()
        WebDriverWait(current_web_driver,delay_min).until(expected_conditions.visibility_of(self.action_result_message))
        return

    def method_home_page_navigate_to_register(self, current_web_driver):
        self.link_register.click()
        WebDriverWait(current_web_driver, delay_medium).until(expected_conditions.title_contains('Register for Free'))
        return
