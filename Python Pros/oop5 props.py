# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Person(object):
    def __init__(self, name):
        self.name=name
      
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name=name
      
    # this is a property, not a method!!!!
    @property
    def show_details(self):
        return '{} {}'.format(self.name, 'is the best!')
        
p1=Person('Jack')
print(p1.name)
print(p1.show_details)