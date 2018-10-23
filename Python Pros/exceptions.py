# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:23:25 2018

@author: Stefan Draghici
"""

try:
    f=open('test_file.txt')
except Exception:
    print('File does not exist.')