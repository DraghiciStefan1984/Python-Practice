# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:04:58 2018

@author: Stefan Draghici
"""

class MyClass(object):
    _instance=None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super(MyClass, cls)
        return cls._instance


obj1=MyClass()
obj2=MyClass()

print(id(obj1))
print(id(obj2))