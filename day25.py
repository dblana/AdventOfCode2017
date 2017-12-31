# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:34:36 2017

@author: Dimitra
"""

def step(state,pos,tape):
    '''Steps of Turing machine'''

    if pos not in tape:
        tape[pos] = 0
        
    current_value = tape[pos]
           
    if state == 'A':
        if current_value == 0:
            tape[pos] = 1
            pos += 1
            new_state = 'B'
        else:
            tape[pos] = 0
            pos += 1
            new_state = 'F'

    if state == 'B':
        if current_value == 0:
            pos -= 1
            new_state = 'B'
        else:
            pos -=1
            new_state = 'C'

    if state == 'C':
        if current_value == 0:
            tape[pos] = 1
            pos -= 1
            new_state = 'D'
        else:
            tape[pos] = 0
            pos += 1
            new_state = 'C'

    if state == 'D':
        if current_value == 0:
            tape[pos] = 1
            pos -= 1
            new_state = 'E'
        else:
            pos += 1
            new_state = 'A'

    if state == 'E':
        if current_value == 0:
            tape[pos] = 1
            pos -= 1
            new_state = 'F'
        else:
            tape[pos] = 0
            pos -= 1
            new_state = 'D'

    if state == 'F':
        if current_value == 0:
            tape[pos] = 1
            pos += 1
            new_state = 'A'
        else:
            tape[pos] = 0
            pos -= 1
            new_state = 'E'
            
    return new_state, pos, tape


tape ={}
state = 'A'
pos = 0
nsteps = 12964419
#nsteps = 5

for i in range(nsteps):
    state,pos,tape = step(state,pos,tape)
    
print(sum(tape.values()))

