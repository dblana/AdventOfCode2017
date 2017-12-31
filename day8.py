# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:08:32 2017

@author: Dimitra
"""

#line = 'sdj dec 558 if r <= 8'
registers = {}
max_value = 0

with open('day8_input.txt') as f:
    for line in f:
        print(line)
        line_parts = line.split(' if ')
        var_name,inc_dec,amount = line_parts[0].split()
        condition = line_parts[1]
        var_name_2,comparison,num = condition.split()
        
        if var_name not in registers.keys():
            registers[var_name] = 0
                
        if var_name_2 not in registers.keys():
            registers[var_name_2] = 0
                     
        condition = eval(str(registers[var_name_2])+comparison+num)
        if condition:
            if inc_dec == 'inc':
                registers[var_name] += int(amount)
            else:
                registers[var_name] -= int(amount)
        if max(registers.values()) > max_value:
            max_value = max(registers.values())
            
print(max(registers.values()))
print(max_value)