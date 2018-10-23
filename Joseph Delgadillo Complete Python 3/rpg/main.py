# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 13:06:29 2018

@author: Stefan Draghici
"""

from game import Person, BgColors

magic=[{'name':'fire', 'cost':10, 'dmg':60},
       {'name':'thunder', 'cost':15, 'dmg':80},
       {'name':'blizzard', 'cost':8, 'dmg':50}]

player=Person(460, 65, 60, 34, magic)
enemy=Person(1200, 65, 45, 25, magic)

running=True

print(BgColors.FAIL+BgColors.BOLD+"An enemy attacks!!!"+BgColors.ENDC)

while running:
    print('===========================')
    player.choose_action()
    choice=input("Choose action: ")
    index=int(choice)-1
    
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print('You attacked for', dmg,'damage points. Enemy HP:', enemy.get_hp())
        
    enemy_choice=1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print('Enemy attacked for', enemy_dmg,'damage points. Player HP:', player.get_hp())