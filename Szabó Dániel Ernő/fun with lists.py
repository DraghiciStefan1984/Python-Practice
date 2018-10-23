# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 00:11:42 2018

@author: Stefan Draghici
"""

a_list=[]
another_list=list()

even_nums=[]

for i in range(100):
    if i%2==0:
        even_nums.append(i)
        
print(even_nums)

odd_nums=[i for i in range(100) if i%2==1]

print(odd_nums)