# -*- coding: utf-8 -*-
########################
#   Project: AzisabaCommander
#   Author: testusuke
#   Class: Grep
#   Date: 2020/2/23
########################

import sys

optionList = ['natural','ignore','and','or']

def grep(path, option, *args):
    with open(path) as f:
        lines = f.readlines()
    # option
    if option == ''

def existOption(option):
    return str(option) in optionList