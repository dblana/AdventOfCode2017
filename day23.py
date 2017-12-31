# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:16:39 2017

@author: Dimitra
"""
import re

registers = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,}
instructions = []

def value_of(Y,registers):
    '''returns Y if Y is an integer, 
    and the value of Y if Y is one of the registers'''
    if Y in registers:
        return registers[Y]
    else:
        return int(Y)
    
def run_instr(instruction,X,Y,registers):
    '''runs the instruction on Y and Y'''
    if instruction == 'set':
        return value_of(Y,registers)
    elif instruction == 'sub':
        return registers[X] - value_of(Y,registers)
    else:
        return registers[X] * value_of(Y,registers)

with open('day23_input.txt') as f:
    for line in f:
        instructions += [line]

index = 0
ntimes = 0

while index<len(instructions):   
    instruction,X,Y = instructions[index].split()
    if instruction == 'mul':
        ntimes +=1
    if instruction == 'jnz':
        if value_of(X,registers) != 0:
            index += int(Y)
        else:
            index +=1
    else:
        registers[X] = run_instr(instruction,X,Y,registers)
        index +=1

print(ntimes)

#################################

#my_primes = []
#with open('primes.txt') as f:
#    for line in f:
#        numbers = [int(s) for s in re.findall(r'\d+',line)]
#        for num in numbers:
#            my_primes.append(num)
        
b = 106500
c = 123500

h = 0
runs = 0

while 1:
    runs += 1
#    if b not in my_primes:
#        h +=1

    d = 2
    f = 0
    while d<b:
        if b % d == 0:
            f=1
            break
        d +=1
    if f:
        h +=1
        
    if b==c:
        break
    
    b += 17

print(h)