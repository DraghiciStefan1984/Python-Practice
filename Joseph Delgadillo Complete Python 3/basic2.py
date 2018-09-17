# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:44:45 2018

@author: Stefan Draghici
"""

def func(arg1):
    print(arg1*5)
    
func(3)
func('dfs')

# default arguments
def default_args(name='Stefan', age=33):
    print("My name is "+name+", and I am "+str(age)+" years old.")
    
default_args()
default_args('Bogdan', 45)

# *args arguments
def print_people(*people):
    for person in people:
        print(person)

print_people('Mike', 'John', 'Mary')