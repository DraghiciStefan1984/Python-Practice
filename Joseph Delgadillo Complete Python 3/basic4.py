# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:06:20 2018

@author: Stefan Draghici
"""

import random

class Enemy():
    hp=200
    
    def __init__(self, attack_low, attack_high):
        self.attack_low=attack_low
        self.attack_high=attack_high
    
    def get_attack(self):
        print(random.randint(self.attack_low, self.attack_high))
        
    def getHP(self):
        print(self.hp)
    
enemy1=Enemy(10, 50)
enemy1.get_attack()
enemy1.getHP()

enemy2=Enemy(35, 80)
enemy2.get_attack()
enemy2.getHP()
