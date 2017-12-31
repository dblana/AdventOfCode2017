# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:35:12 2017

@author: Dimitra
"""

import re

layers = {}

with open('day13_input.txt') as f:
    for line in f:
        numbers = [int(s) for s in re.findall(r'\d+',line)]
        layers[numbers[0]] = numbers[1]

severity = [key*value for key, value in layers.items() if not (key % (2*value-2))]
#print(sum(severity))

delay=0
while sum(severity)>0:
    delay+=1
    severity = [1 for key, value in layers.items() if not ((key+delay) % (2*value-2))]
#    print(sum(severity))

print(delay)
