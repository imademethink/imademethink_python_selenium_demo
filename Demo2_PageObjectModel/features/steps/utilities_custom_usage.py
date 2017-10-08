#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


class UtilitiesCustom():

    def __init__(self):
        pass

    def method_utilities_compare_all_success_failure(farg, *args): # variable number of arguments
        for arg in args:
            if isinstance(arg, list):
                for one_element in arg:
                    if 'failure' in str(one_element):
                        raise Exception(' ******* Failure is observed in a particular step')
        print ('All steps were successfully executed')
        return
