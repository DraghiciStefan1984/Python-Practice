# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Fruit(object):
    cost=2
    count=0
    def __init__(self, name):
        self.name=name
        type(self).count+=1
        
    def __del__(self):
        type(self).count-=1
        
    def printer(self, message):
        self.message=message
        print('your message is', self.message)
        
apple=Fruit('apple')
pare=Fruit('paire')
banana=Fruit('banana')

print(apple.name)
print(apple.cost)
print(Fruit.cost)
print('class instances',Fruit.count)

print(apple.printer('I am an apple'))


class Calc():
    def add(self, x, y):
        self.x=x
        self.y=y
        return x+y
        
    def sub(self, x, y):
        self.x=x
        self.y=y
        return x-y
    
    def div(self, x, y):
        self.x=x
        self.y=y
        return x/y
    
    def mult(self, x, y):
        self.x=x
        self.y=y
        return x*y
    
calc=Calc()
print(calc.add(20, 35))