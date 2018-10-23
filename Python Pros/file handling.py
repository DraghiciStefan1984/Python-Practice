# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

# write to a file
file_handle=open('test.txt', 'w')
line='Test text'
file_handle.write(line)
file_handle.close()

# read from a file
file_handle=open('test.txt', 'r')
data=file_handle.read()
print(data)

