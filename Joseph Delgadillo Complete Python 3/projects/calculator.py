# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:49:42 2018

@author: Stefan Draghici
"""

class Calculator():
    def __init__(self):
        self.a=0
        self.b=0
        self.operation=None
        
    def _addition(self, a, b):
        return self.a+self.b
    
    def _subtraction(self, a, b):
        return self.a-self.b
    
    def _division(self, a, b):
        return self.a/self.b
    
    def _multiply(self, a, b):
        return self.a*self.b
    
    def _modulo(self, a, b):
        return self.a%self.b
    
    def calculate(self):
        print("Enter your numbers: ")
        self.a=float(input("x: "))
        self.b=float(input("y: "))
        self.operation=input("Enter the operation (+, -, /, *. %): ")
        
        if self.operation=='+':
            print(self._addition(self.a, self.b))
        elif self.operation=='-':
            print(self._subtraction(self.a, self.b))
        elif self.operation=='/':
            print(self._division(self.a, self.b))
        elif self.operation=='*':
            print(self._multiply(self.a, self.b))
        elif self.operation=='%':
            print(self._multiply(self.a, self.b))
        else:
            print("Invalid operation")
            return
        
calculator=Calculator()
calculator.calculate()