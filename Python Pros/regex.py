# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 13:46:11 2018

@author: Stefan Draghici
"""

import re

paragraph='dasdsuidnfsafdsf dfsafkj. 164 dsfsdab, 1654 dfsfan fsdhf 164. as1846 13 1515 Stefan'

print(re.findall(r'164', paragraph))
print(re.search(r'St....', 'Stefan').group())