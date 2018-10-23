# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Person():
    def __init__(self,name, age, address):
        self.name=name
        self.age=age
        self.address=address
        
    def __str__(self):
        return '{} is {} years young, from {}'.format(self.name, self.age, self.address)
        
person=Person('Stefan', 34, 'Bucharest')
print(person)