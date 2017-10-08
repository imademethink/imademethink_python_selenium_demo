#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step
import sys
from step_impl_handle import *

global_list_variables = []


@given(u'Perform initial browser setup')
def step_impl(context,):
    obj_handle_impl.perform_initial_setup(global_list_variables)


@when(u'Perform some action on home page "{url_home_page}"')
def step_impl(context,url_home_page):
    obj_handle_impl.perform_some_action_on_home_page(global_list_variables, url_home_page)


@when(u'Perform some action on about us page')
def step_impl(context,):
    obj_handle_impl.perform_some_action_on_about_us_page(global_list_variables)


@when(u'Perform some action on admin page')
def step_impl(context,):
    obj_handle_impl.perform_some_action_on_admin_page(global_list_variables,)


@when(u'Perform some action on registration page')
def step_impl(context,):
    obj_handle_impl.perform_some_action_on_registration_page(global_list_variables,)


@then(u'All actions should be successful')
def step_impl(context,):
    obj_handle_impl.final_verification(global_list_variables)
