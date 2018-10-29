# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:57:15 2018

@author: Stefan Draghici
"""

class Animal():
    noise='grunt'
    size='large'
    color='brown'
    hair='covers body'
    
    def get_color(self):
        return self.color
    
    def make_noise(self):
        return self.noise

class Dog(Animal):
    name='Bobby'
    color='brown'
    
    def get_color(self):
        return self.color
    
    def get_name(self):
        return self.name
    
dog1=Animal()
print(dog1.get_color())
print(dog1.make_noise())

dog2=Dog()
dog2.color='white'
dog2.name='Rex' 