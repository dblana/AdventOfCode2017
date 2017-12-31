# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:53:14 2017

@author: Dimitra
"""

import numpy as np

x = 1
y = 0.5


def take_step(current_pos,direction):
    '''Finds new position based on direction of movement'''
    if direction == 's':
        current_pos = current_pos + np.array([0,-1])
    elif direction == 'n':
        current_pos = current_pos + np.array([0,1])
    elif direction == 'ne':
        current_pos = current_pos + np.array([x,y])    
    elif direction == 'nw':
        current_pos = current_pos + np.array([-x,y])
    elif direction == 'se':
        current_pos = current_pos + np.array([x,-y])
    elif direction == 'sw':
        current_pos = current_pos + np.array([-x,-y])    
    return current_pos

pos = np.array([0,0])
furthest_dist = 0

with open('day11_input.txt') as f:
  while True:
    c = f.read(1)
    if not c:      
      break
    step = c
    c = f.read(1)
    while c != ',':        
        step = step + c
        c = f.read(1)
    pos = take_step(pos,step)
    current_dist = np.abs(pos[0])/2 + np.abs(pos[1])
    if current_dist > furthest_dist:
        furthest_dist = current_dist

print(current_dist)
print(furthest_dist)
