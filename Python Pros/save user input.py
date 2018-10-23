# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

# write to a file
file_handle=open('userdata.txt', 'w')
name=input('enter your name: ')
age=input('enter your age: ')
file_handle.write('Username is: %s\n'%name)
file_handle.write('Age is: %s\n'%str(age))