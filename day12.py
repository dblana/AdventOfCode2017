# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:49:08 2017

@author: Dimitra
"""

import re

#line = '7 <-> 7, 959'
programs = {}

with open('day12_input.txt') as f:
    for line in f:
        numbers = [int(s) for s in re.findall(r'\d+',line)]
        programs[numbers[0]] = numbers[1:]

def add_connection(new_program, connected_list):
    '''Check if the program is already in the list. If it is, return. 
    If it is not, add it to the list and run add_connection on its connections
    '''
    if new_program not in connected_list:
        connected_list.append(new_program)
        for con_programs in programs[new_program]:
            connected_list = add_connection(con_programs, connected_list)            
    return connected_list


complete_list = add_connection(0,[])
print(len(complete_list))
num_groups = 1

for oneprog in programs:
    if oneprog not in complete_list:
        complete_list += add_connection(oneprog,[])
        num_groups +=1
        print(len(complete_list))

print(num_groups)