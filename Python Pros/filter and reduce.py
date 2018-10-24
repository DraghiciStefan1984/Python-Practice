# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:23:25 2018

@author: Stefan Draghici
"""
from functools import reduce

values=[1,2,3,4,5,6,7,8,9]
result=[]

'''
for i in values:
    if i%2==0:
        result.append(i)
'''

print(filter(lambda x: x%2==0, values))

paragraph='this is the best thing ever!!!'
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','w']
print(filter(lambda letter:letter in paragraph, letters))
print(reduce((lambda letter1, letter2:letter1+letter2), letters))