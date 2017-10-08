#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import *


def before_all(context):
    pass
    #   print ('=====Before ALL=====')


def after_all(context):
    pass
    #    print ('=====After ALL=====')


def before_feature(context, feature):
    if 'Decorators feature 2' in str(feature):
        print ('====Before Feature====' + str(feature))


def after_feature(context, feature):
    if 'Decorators feature 2' in str(feature):
        print ('====After Feature====' + str(feature))


def before_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===Before Scenario===' + str(scenario))


def after_scenario(context, scenario):
    if 'Decorators check case 4' in str(scenario):
        print ('===After Scenario===' + str(scenario))


def before_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==Before Step==' + str(step))


def after_step(context, step):
    if 'I start decorators check case 2' in str(step):
        print ('==After Step==' + str(step))


def before_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=Before Tag=' + str(tag))


def after_tag(context, tag):
    if 'tag1' in str(tag):
        print ('=After Tag=' + str(tag))
