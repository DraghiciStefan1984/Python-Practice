# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:01:53 2018

@author: Stefan Draghici
"""

def func(num):
    return num+1

var=func(13)
print(var)

var2=func
print(var2)

def function_one(func):
    print('function one')
    func()
    
def function_two():
    print('function two')
    
print(function_one(function_two))

###################################################

def my_dec(printer):
    def my_printer(*args, **kwargs):
        print('this is my printer')
        return printer(*args, **kwargs)
    return my_printer

@my_dec
def show():
    print('this is my show func')
    
show()
var=my_dec(show)
print(var)

@my_dec
def show_with_params(num, string):
    print('you passed {} and {}'.format(num, string))
    
show_with_params(35, 'hgdas')

###################################################

class Decor(object):
    def __init__(self, printer):
        self.printer=printer
        
    '''Must use call if we want tu use the class as a decorator'''
    def __call__(self, *args, **kwargs):
        print('This is call from Decor class.')
        return self.printer(*args, **kwargs)

@Decor
def show_class():
    print('this is my show_class func')
      
show_class()