# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 15:43:03 2018

@author: Stefan Draghici
"""

if (5>3):
    print("hello")
else:
    print("bye")
    
if (45>50 and 33==21):
    print("run")
    
list1=[1,5,6,3,2,6,5,3,5,1]

for item in list1:
    print(item)
    
print('#######################')
    
for item in list1:
    if item%2==0:
        print(item)
        
print('#######################')
        
for i in range(2, 200, 3):
    print(i)
    
###################################################

counter=0

while counter<50:
    print(counter)
    counter+=1
    
while counter<25:
    print(counter)
    if counter==5:
        break
    counter+=1
    
while counter<25:
    counter+=1
    if counter==5:
        continue
    print(counter)
