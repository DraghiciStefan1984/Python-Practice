# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Fruit(object):
    def __init__(self, name):
        pass
        
    def set_name(self, name):
        self.__name=name
        
    def get_name(self):
        return self.__name
        
fruit=Fruit('Banana')
fruit.set_name('cherry')
print(fruit.get_name())