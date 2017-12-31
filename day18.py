# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:15:42 2017

@author: Dimitra
"""

registers = {}

line = 'jgz b -1'
instructions = []

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

with open('day18_input.txt') as f:
    for line in f:
        instructions += [line]
        line_parts = line.split()
        for part in line_parts[1:]:
            if not check_int(part) and part not in registers:
                registers[part] = 0
        
index = 0

while index<len(instructions):   
     
    line_parts = instructions[index].split()
    if line_parts[0] =='snd':
        sound_played = registers[line_parts[1]]
        index +=1
    elif line_parts[0] == 'set':
        if line_parts[2] not in registers:
            registers[line_parts[1]] = int(line_parts[2])
        else:
            registers[line_parts[1]] = registers[line_parts[2]]
        index +=1
    elif line_parts[0] == 'add':
        if line_parts[2] not in registers:
            registers[line_parts[1]] += int(line_parts[2])
        else:
            registers[line_parts[1]] += registers[line_parts[2]]
        index +=1
    elif line_parts[0] == 'mul':
        if line_parts[2] not in registers:
            registers[line_parts[1]] *= int(line_parts[2])
        else:
            registers[line_parts[1]] *= registers[line_parts[2]]
        index +=1
    elif line_parts[0] == 'mod':
        if line_parts[2] not in registers:
            registers[line_parts[1]] = registers[line_parts[1]] % int(line_parts[2])
        else:
            registers[line_parts[1]] = registers[line_parts[1]] % registers[line_parts[2]]
        index +=1
    elif line_parts[0] == 'rcv':
        if registers[line_parts[1]] != 0:
            print(sound_played)
            break
    else:
        if registers[line_parts[1]] > 0:
            index += int(line_parts[2])
        else:
            index +=1
    print(index)
                
        