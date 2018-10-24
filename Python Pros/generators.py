# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:01:53 2018

@author: Stefan Draghici
"""

def gen():
    name='Stefan'
    age=34
    dob='04-10-1984'
    '''when we use yield inside a function it becomes a generator that will return an iterator'''
    yield name, age, dob
    
print(gen())

iterator=gen()
print(iterator.__next__())
