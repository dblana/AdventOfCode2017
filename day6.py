# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:17:08 2017

@author: Dimitra
"""

input_str = '10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6'
input_list = input_str.split()
state = list(map(int, input_list))

#state = [0,2,7,0]

lbank = len(state)
    
all_configs = []
num_steps = 0

while state not in all_configs:
    num_steps +=1
    all_configs.append(state)
    numblocks = max(state)
    bank = state.index(numblocks)    
    state = list(state)
    state[bank]=0
    for i in range(numblocks):
        ibank = bank+i+1
        ibank = ibank % lbank
        state[ibank] +=1

print(num_steps)

loop_state = list(state)
numblocks = max(loop_state)
bank = loop_state.index(numblocks)    
loop_state[bank]=0
for i in range(numblocks):
    ibank = bank+i+1
    ibank = ibank % lbank
    loop_state[ibank] +=1

size_loop = 1

while loop_state != state:
    size_loop +=1
    numblocks = max(loop_state)
    bank = loop_state.index(numblocks)    
    loop_state[bank]=0
    for i in range(numblocks):
        ibank = bank+i+1
        ibank = ibank % lbank
        loop_state[ibank] +=1

print(size_loop)