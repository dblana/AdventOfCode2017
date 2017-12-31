# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 10:31:32 2017

@author: Dimitra
"""

components = []
with open('day24_input.txt') as f:
    for line in f:
        p1, p2 = [int(x) for x in line.split('/')]
        components.append((p1,p2))

max_strength = 0
max_length = 0
strength_at_max_length = 0

def build_bridge(port,comp_list,strength,length):
    '''builds bridge from components with appropriate ports'''
    global max_strength
    global max_length
    global strength_at_max_length
    
    in_port = 0
    for comp in comp_list:
        if port in comp:
            in_port +=1
            my_strength = strength + sum(comp)
            my_length = length + 1
            my_list = list(comp_list)
            my_list.remove(comp)
            if port == comp[0]:
                other_port = comp[1]
            else:
                other_port = comp[0]
            build_bridge(other_port,my_list,my_strength,my_length)
    if in_port == 0:
        if strength > max_strength:
            max_strength = strength
        if length > max_length:
            max_length = length
            strength_at_max_length = strength
        elif length == max_length:
            if strength > strength_at_max_length:
                strength_at_max_length = strength
            
        
build_bridge(0,components,0,0)
print(max_strength)
print(strength_at_max_length)

    