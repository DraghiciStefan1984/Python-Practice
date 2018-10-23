# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:42:28 2018

@author: Stefan Draghici
"""

def print_something1(name, age):
    print('My name is '+name+', I am '+str(age)+' years old.')
    
def print_something2(name, age):
    print('My name is ',name, ', I am ', age, ' years old.')
    
def print_people(*people):
    for person in people:
        print(person)
    
print(print_something1('Stefan', 25))
print(print_something2('Stefan', 25))

print(print_something1(age=28, name='Nick'))

print(print_people('adsasda', 'ssfg', 'dasad'))