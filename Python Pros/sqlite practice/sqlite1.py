# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 11:02:59 2018

@author: Stefan Draghici
"""
 
import sqlite3

connection=sqlite3.connect("test.db")
#query_executor=connection.execute('''CREATE TABLE test_table(id INT PRIMARY KEY NOT NULL, username TEXT);''')
#connection.execute('''INSERT INTO test_table(id, username) VALUES(101, "Stefan");''')
#connection.commit()

db_object=connection.execute('''SELECT id, username FROM test_table''')

for data in db_object:
    print(data[0], data[1])