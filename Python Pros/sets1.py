# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:23:25 2018

@author: Stefan Draghici
"""


first_set={1,2,3,4,5,8}
second_set={6,7,8,9,10,4,2}

union=first_set | second_set
print('union =', union)

intersection=first_set & second_set
print('intersection =', intersection)

difference=first_set - second_set
print('difference =', difference)

symetric_difference=first_set ^ second_set
print('symetric_difference =', symetric_difference)

##########################   map and zip   #####################

my_list=['fdsf', 'dsaa', 'feergtet', 'ryttry']
other_list=[1,2,3,5,4,1,3]

def printer(message):
    print(message)

my_map=map(printer, my_list)
print(my_map)

my_zip=zip(my_list, other_list)
print(my_zip)