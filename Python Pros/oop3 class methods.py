# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Book(object):
    # private attribute
    __writer_name='Stefan'
    __reader_name='James'
    
    # class method
    @classmethod
    def writer(cls):
        return Book.__writer_name
    
    def reader(self):
        return self.__reader_name
    
print(Book.writer())

book=Book()
print(book.reader())
print(book.writer())