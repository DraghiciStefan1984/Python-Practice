# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class A:
    def m(self):
        print('This is from A')
        
    def m1(self):
        print('m1 method')
        
class B(A):
    def m(self):
        print('This is form B')
        super().m()
        
class C():
    def printer(self):
        print('This is first.')
      
    '''this does not work
    def printer(self, name):
        self.name=name
        print('This is second {}'.format(self.name))
    '''
        
b1=B()
b1.m()
b1.m1()