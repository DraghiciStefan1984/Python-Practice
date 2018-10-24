# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 12:48:27 2018

@author: Stefan Draghici
"""

with open('text_file.txt', 'w') as my_file:
    my_file.write('with')

class ContextManager(object):
    def __init__(self, file_name, mode):
        self.f_obj=open(file_name, mode)
        
    def __enter__(self):
        return self.f_obj
    
    def __exit__(self, type, value, trackback):
        self.f_obj.close()
        
with ContextManager(my_file, 'w') as object:
    object.write('this a context manager')