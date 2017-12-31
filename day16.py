# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 10:05:11 2017

@author: Dimitra
"""

import csv
with open('day16_input.txt', 'r') as csvfile:
    reader = csv.reader(csvfile)
    dance_moves = next(reader)

#dance_moves = ['s1','x3/4','pe/b']
#progs = [chr(97+i) for i in range(5)]

progs = [chr(97+i) for i in range(16)]
all_progs = [''.join(progs)]

for i in range(100):
    
    for move in dance_moves:
        if move[0]=='p':
            A = progs.index(move[1])
            B = progs.index(move[3])
            save_elem = progs[A]
            progs[A] = progs[B]
            progs[B] = save_elem        
        elif move[0]=='x':
            A,B = move[1:].split('/')
            save_elem = progs[int(A)]
            progs[int(A)] = progs[int(B)]
            progs[int(B)] = save_elem
        else:
            num_spin = int(move[1:])
            progs2move = list(progs[-num_spin:])
            del progs[-num_spin:]
            progs = progs2move + progs

    new_prog = ''.join(progs)
    if new_prog in all_progs:
        break
    else:
        all_progs += [''.join(progs)]

# The outcomes repeat after a while. To find the outcome after a billion
# iterations, we find the frequency of same outputs, and the remainder
# when divided by a billion

index = 1000000000 % len(all_progs)
print(all_progs[index])