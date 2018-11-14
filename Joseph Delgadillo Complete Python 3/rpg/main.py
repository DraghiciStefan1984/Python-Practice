# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:51:22 2018

@author: Stefan Draghici
"""

from classes.game import Person, Bcolors

magic=[{'name':'Fire', 'cost':10, 'dmg':60}, 
       {'name':'Thunder', 'cost':15, 'dmg':80}, 
       {'name':'Blizzard', 'cost':8, 'dmg':40}]

player=Person(460, 65, 60, 34, magic)
enemy=Person(1200, 65, 45, 25, magic)

running=True
print(Bcolors.FAIL+Bcolors.BOLD+"Enemy attacks!"+Bcolors.ENDC)

while(running):
    print("===============================")
    player.choose_action()
    choice=input("Choose action: ")
    index=int(choice)-1
    
    if index==0:
        dmg=player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points if damage, enemy hp:", enemy.get_hp())
    elif index==1:
        player.choose_spell()
        magic_choice=int(input("Choose magic:"))-1
        magic_dmg=player.generate_spell_damage(magic_choice)
        spell=player.get_spell_name(magic_choice)
        cost=player.get_spell_mp_cost(magic_choice)
        current_mp=player.get_mp()
        if cost>current_mp:
            print("You don't have enough mp!")
            continue
        
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(spell+" deals", str(magic_dmg), " point of damage.")
        
    enemy_choice=1
    enemy_dmg=enemy.generate_damage()
    player.take_damage(enemy_dmg)
    
    print("Enemy attacks for", enemy_dmg, "points if damage, player hp:", player.get_hp())
    print("Enemy HP:", str(enemy.get_hp())+"/"+str(enemy.get_max_hp()))
    print("Player HP:", str(player.get_hp())+"/"+str(player.get_max_hp()))
    
    if enemy.get_hp()==0:
        print("You win!")
        running=False
    elif player.get_hp()==0:
        print("You lose!")
        running=False