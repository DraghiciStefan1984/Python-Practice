# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:29:49 2018

@author: Stefan Draghici
"""

import simplejson as json
import os

if os.path.isfile("/.ages.json") and os.stat("/.ages.json").st_size != 0:
    old_file=open("/.ages.json", "r+")
    data=json.loads(old_file.read())
    print("Current age is:", data["age"], "-- adding a year.")
    data["age"]=data["age"]+1
    print("New age is", data["age"])
else:
    old_file=open("/.ages.json", "w+")
    data={"name":"Bob", "age":33}
    print("No file found found, creating new file.")
    
old_file.seek(0)
old_file.write(json.dumps(data))