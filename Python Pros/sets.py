# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:23:25 2018

@author: Stefan Draghici
"""

blank_set=()
first_set=set([1,2,3,6,5,5,4,7])
second_set={1,2,3,1,5,5,6,3,3,1,1}

print(first_set)
print(second_set)

'''this will not work
print(first_set[2])
second_set.add(2, 5)'''

second_set.add(22)
second_set.add(2)
print(second_set)

first_set.update([22, 45, 30])
print(first_set)