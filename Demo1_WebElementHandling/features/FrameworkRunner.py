#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    # run Behave + BDD + Python code
    featureFilePath = ' feature_files_folder/Demo_Web_Elements.feature '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)
