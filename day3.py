# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:23:16 2017

@author: Dimitra
"""

magic_num = 277678

#magic_num = 1024

# Find number that if squared is just over magic_num
side_length=0
while (side_length**2)<magic_num:
    side_length=side_length+1

print(side_length)

from_the_corner = side_length**2 - magic_num

print(from_the_corner)

travel = side_length - from_the_corner

print(travel-1)

# Part 2: https://oeis.org/A141481
# https://oeis.org/A141481/b141481.txt