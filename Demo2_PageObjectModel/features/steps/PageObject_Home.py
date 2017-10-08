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


class HomePage(PageObject):
    text_box_username = PageElement(name='username')
    text_box_password = PageElement(name='password')
    link_about_us = PageElement(css="a[href='about.htm']")
    button_login = PageElement(css="input[type='submit']")

    def method_home_page_launch_home_url(self, current_web_driver, url_home_page):
        self.get(url_home_page)
        # time.sleep(delay_max)
        WebDriverWait(current_web_driver,delay_max).until(expected_conditions.title_contains('Welcome'))
        return

    def method_home_page_login(self, current_web_driver):
        self.text_box_username = 'admin'
        self.text_box_password = 'password'
        self.button_login.click()
        WebDriverWait(current_web_driver, delay_medium).until(expected_conditions.title_contains('Error'))
        return

    def method_home_page_navigate_to_about_us(self, current_web_driver):
        self.link_about_us.click()
        WebDriverWait(current_web_driver, delay_medium).until(expected_conditions.title_contains('About Us'))
        return

