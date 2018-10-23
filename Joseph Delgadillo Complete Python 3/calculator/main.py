# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:53:34 2018

@author: Stefan Draghici
"""

import re

print("The calculator!!!")
print("Type 'quit' to exit.\n")
previous=0
run=True

def perform_math():
    global run
    global previous
    equation=''
    
    if previous==0:
        equation=input("Enter the equation: ")
    else:
        equation=input(str(previous))
    
    if equation=='quit':
        run=False
    else:
        equation=re.sub('[a-zA-Z,.()" "]', '', equation)
        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)
    
while run:
    perform_math()