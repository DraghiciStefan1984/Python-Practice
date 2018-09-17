# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 17:06:20 2018

@author: Stefan Draghici
"""

import random

player_hp=300
enemy_attack_low=40
enemy_attack_high=80

while player_hp>=0:
    damage=random.randrange(enemy_attack_low, enemy_attack_high)
    player_hp-=damage
    print("Player takes: ", damage, " damage.")
    
    if player_hp<50 or player_hp>=60:
        continue
    if player_hp<=20:
        print("Player has: ", player_hp, " hp left.")
        break