# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

import copy

class Point():
    pass

p1=Point()
p2=p1

print(p1)
print(p2)
print(Point)

p1.x=11
p1.y=22
print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1==p2)
print(p1 is p2)

p3=copy.copy(p1)
print(p1==p3)
print(p1 is p3)