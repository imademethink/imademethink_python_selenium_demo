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


class AboutUsPage(PageObject):
    plain_text = PageElement(xpath='//*[@id="rightPanel"]/p[2]')
    link_admin = PageElement(css="a[href='admin.htm']")

    def method_verify_specific_message(self, current_web_driver, messge1, messge2):
        actual_text = self.plain_text.text
        if messge1 not in actual_text:
            raise Exception(' ******* Following expected "' + messge1 + '" text is not found in ' + actual_text)
        if messge2 not in actual_text:
            raise Exception(' ******* Following expected "' + messge2 + '" text is not found in ' + actual_text)
        return

    def method_about_us_navigate_to_admin(self, current_web_driver):
        self.link_admin.click()
        WebDriverWait(current_web_driver, delay_medium).until(expected_conditions.title_contains('Administration'))
        return
