# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:58:50 2018

@author: Stefan Draghici
"""

def tuple_data(a, *b):
    print(a)
    print(b)
    
print(tuple_data('a', 1,3,8,5,4,6))

def dict_data(**d):
    print(d)
    
print(dict_data(name='Stefan', age=30))

def f1(a, *b, **c):
    print('a is', a)
    print('b is', b)
    print('c is', c)
    
print(f1(1,4,3,5,3,8, name='Stefan', age=30))

var=lambda x, y, z: x+y+z
print(var(1,2,3))

def func1(x): return x+2
def func2(x): return x*2
def func3(x): return x//2

func_list=[func1, func2, func3]
for func in func_list:
    print(func(4))
    
print('\n\n==========================\n\n')
    
lambda_list=[lambda x:x+2, lambda x:x*2, lambda x:x//2]
for func in lambda_list:
    print(func(4))