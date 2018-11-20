# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 19:51:22 2018

@author: Stefan Draghici
"""

from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item

fire=Spell("Fire", 10, 60, "black")
thunder=Spell("Thunder", 15, 80, "black")
blizzard=Spell("Blizzard", 8, 40, "black")
meteor=Spell("Meteor", 20, 100, "black")
quake=Spell("Quake", 5, 25, "black")
cure=Spell("Cure", 12, 120, "white")
cura=Spell("Cura", 18, 200, "white")

potion=Item("Potion", "potion", "heals 50hp", 50)
hi_potion=Item("Hi-Potion", "potion", "heals 100hp", 100)
super_potion=Item("Super Potion", "potion", "heals 500hp", 500)
elixer=Item("Elixer", "elixer", "fully restores hp of one party member", 900)
mega_elixer=Item("Mega Elixer", "elixer", "fully restores hp of all party member", 2000)
grenade=Item("Grenade", "attack", "deals 500 damage.", 500)

player_magic=[fire, thunder, blizzard, meteor, quake, cure, cura]
player_items=[potion, hi_potion, super_potion, elixer, mega_elixer, grenade]

player=Person(460, 65, 60, 34, player_magic, player_items)
enemy=Person(1200, 65, 45, 25, [], [])

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
        
        if magic_choice==-1:
            continue
        
        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()
        
        current_mp=player.get_mp()
        if spell.cost>current_mp:
            print("You don't have enough mp!")
            continue
        
        player.reduce_mp(spell.cost)
        
        if spell.spell_type=="white":
            player.heal(magic_dmg)
            print(spell.name, "heals for", str(magic_dmg), "HP.")
        
        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(spell+" deals", spell.name, " point of damage.")
        
    elif index==2:
        player.choose_item()
        item_choice=int(input("Choose item: "))-1
        
        if item_choice==-1:
            continue
        
        item=player.items[item_choice]
        
        if item.item_type=="potion":
            player.heal(item.prop)
            print(item.name, "heals for", item.prop, "health points")
        
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