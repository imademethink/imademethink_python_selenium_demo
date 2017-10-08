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


class RegistrationPage(PageObject):
    text_box_first_name = PageElement(id_='customer.firstName')
    button_submit_form = PageElement(css="input[value='Register']")
    form_submit_result_message = PageElement(id_='customer.lastName.errors')

    def method_registration_page_clean_database(self, current_web_driver,):
        self.text_box_first_name = 'name_first'
        self.button_submit_form.click()
        WebDriverWait(current_web_driver,delay_medium).until(expected_conditions.visibility_of(self.form_submit_result_message))
        return
