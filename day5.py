# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:05:44 2017

@author: Dimitra
"""

# Import package
import numpy as np

# Assign filename to variable: file
file = 'day5_input.txt'

################## Q1 #########################

# Load file as array: digits
# digits = np.loadtxt(file, dtype=int)

digits = [0,3,0,1,-3]

current_pos=0
steps=0
while current_pos<len(digits):
    new_pos = current_pos + digits[current_pos]
    digits[current_pos] +=1
    current_pos = new_pos
    steps +=1

print(steps)

################## Q2 ##########################

# Load file as array: digits
digits = np.loadtxt(file, dtype=int)

#digits = [0,3,0,1,-3]

current_pos=0
steps=0
while current_pos<len(digits):
    new_pos = current_pos + digits[current_pos]
    if digits[current_pos]>=3:
        digits[current_pos] -=1
    else:
        digits[current_pos] +=1
    current_pos = new_pos
    steps +=1

print(steps)