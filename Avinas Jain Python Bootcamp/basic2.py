# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

shopping_list=['apples', 'oranges', 'cheese', 'meat']

print(shopping_list[2])
print(shopping_list[1:3])
print(shopping_list[1:-2])

shopping_list.append('water')
shopping_list.append('bread')

print(shopping_list[:3])

shopping_list[2]='cake'

del shopping_list[4]

print(shopping_list)

################################################################

students={"Bob":15, "Charlie":18, "Rachel":20, "Emily":13}

print(students)
print(students["Bob"])

################################################################

user_details=("username", "password", 18)

print(user_details)
print(user_details[1])

tup1=("sdf", "sdsfs")
tup2=("ioiu", "zcxz")
tup3=tup1+tup2

print(tup3)