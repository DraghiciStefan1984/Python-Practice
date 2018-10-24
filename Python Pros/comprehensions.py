# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:23:25 2018

@author: Stefan Draghici
"""

# list
list_comp_1=[i for i in range(200)]
print(list_comp_1)

list_a=[1,2,3,4]
list_b=[5,6,7,8]
result_list=[]

# set
set_a={1,2,3,4}
set_b={5,6,7,8}
result_set={(x, y) for x in set_a for y in set_b}
print(result_set)
result_set={x+y for x in set_a for y in set_b}
print(result_set)

# dict
dict_1={'dada':125, 'rtre':7856, 'ewrtret':5314}
dict_2={'eewrtete':1251, 'dsstrtyr':8936, 'dttyrut':8934}
merged_dict={k:v for i in (dict_1, dict_2) for k,v in i.items()}
print(merged_dict)