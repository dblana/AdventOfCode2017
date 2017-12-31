# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 13:06:59 2017

@author: Dimitra
"""

def count_samenum(data):
    '''Find the sum of all digits that match the next digit in the list'''    
    result = 0
    current_num = int(data[-1])
    for ichar in range(len(data)):
        new_num = int(data[ichar])
        if new_num == current_num:
            result += new_num
        current_num = new_num
    return result

def count_halfwaynum(data):
    '''Find the sum of all digits that match the digit halfway around the circular list'''    
    result = 0
    hw = int(len(data)/2)
    hw_data = data[hw:] + data[:hw]

    for ichar in range(len(data)):
        if data[ichar] == hw_data[ichar]:
            result += int(data[ichar])

    return result

#print(count_halfwaynum('1212'))
#print(count_halfwaynum('1221'))
#print(count_halfwaynum('123425'))
#print(count_halfwaynum('123123'))
#print(count_halfwaynum('12131415'))

file = 'day1_input.txt'
file_data = open(file).read()
print(count_halfwaynum(file_data))