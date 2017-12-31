# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:06:14 2017

@author: Dimitra
"""

# Import package
import numpy as np

# Assign filename to variable: file
#file = 'day2_test_input2.txt'
file = 'day2_input.txt'

# Load file as array: digits
digits = np.loadtxt(file, dtype=int, delimiter='\t')
max_nums = digits.max(axis=1)
min_nums = digits.min(axis=1)
line_diff = max_nums - min_nums
print(line_diff.sum())

def evenly_divides(mylist):
    '''find the only two numbers in a 1-D array where one evenly divides the other
    and return the result of the division'''
    for number in mylist:
        list_remainder = np.remainder(mylist, number)
        lucky_num = mylist[list_remainder==0]
        if len(lucky_num)==2:
            return np.divide(lucky_num,number).max()

results = np.apply_along_axis(evenly_divides,1,digits)
print(results.sum())