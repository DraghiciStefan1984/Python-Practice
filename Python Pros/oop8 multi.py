# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class BatsMan:
    def __init__(self, name):
        self.__batsman_name=name
        
    def get_batsman_name(self):
        return self.name
    
    def set_batsman_name(self, name):
        self.__batsman_name=name
        
class Bowler:
    def __init__(self, name):
        self.__bowler_name=name
        
    def get_bowler_name(self):
        return self.name
    
    def set_bowler_name(self, name):
        self.__bowler_name=name
        
class Keeper:
    def __init__(self, name):
        self.__keeper_name=name
        
    def get_keeper_name(self):
        return self.name
    
    def set_keeper_name(self, name):
        self.__keeper_name=name
        
class Player(BatsMan, Bowler, Keeper):
    def __init__(self, player_name):
        BatsMan.__init__(self, player_name)
        Bowler.__init__(self, player_name)
        Keeper.__init__(self, player_name)
        
p1=Player('Tony')
print(p1.get_batsman_name())