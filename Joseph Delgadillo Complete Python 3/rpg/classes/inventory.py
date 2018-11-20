# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:51:03 2018

@author: Stefan Draghici
"""

class Item(object):
    def __init__(self, name, item_type, descr, prop):
        self.name=name
        self.item_type=item_type
        self.descr=descr
        self.prop=prop