# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 18:59:40 2018

@author: Stefan Draghici
"""

class Person():
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name
      
    def get_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
class Employee(Person):
    def __init__(self, first_name, last_name, emp_id, department):
        Person.__init__(self, first_name, last_name)
        self.emp_id=emp_id
        self.department=department
        
    def get_details(self):
        return '{} {}, {}, {}'.format(self.first_name, self.last_name, self.emp_id, self.department)
    
p1=Person('Stefan', 'cel Mare')
print(p1.get_name())

emp1=Employee('Bogdan', 'Unul', 136542, 'marketing')
print(emp1.get_details())