# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:36:24 2017

@author: Dimitra
"""

garbage = False
score = 0
level = 1
total_garbage = 0

with open('day9_input.txt') as f:
  while True:
    c = f.read(1)
    if not c:      
      break
    if c=='!':
        c = f.read(1)
        continue
    
    if garbage and c!='>':
        total_garbage +=1
        
    if c=='{' and not garbage:
        score += level
        level += 1
    elif c=='}' and not garbage:
        level -= 1
    elif c=='<':
        garbage = True
    elif c=='>':
        garbage = False

print(score)
print(total_garbage)