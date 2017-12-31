# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 08:59:21 2017

@author: Dimitra
"""

A = 512
B = 191

#A = 65
#B = 8921

A_factor = 16807
B_factor = 48271
divide_by = 2147483647

mask = (1 << 16) - 1
def compare(num1, num2):
    return not (num1 ^ num2) & mask

judge = 0
for i in range(5000000):
    while 1:
        A = (A*A_factor) % divide_by
        if not (A % 4):
            break

    while 1:
        B = (B*B_factor) % divide_by
        if not (B % 8):
            break
        
    judge += compare(A,B)

print(judge)