# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:14:52 2017

@author: Dimitra
"""

import numpy as np

input_lengths = [34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167]
my_length = 256
my_list = np.array(range(my_length))

#input_lengths = [3,4,1,5]
#my_length = 5
#my_list = np.array(range(my_length))

current_position = 0
skip_size = 0

for input_length in input_lengths:
    indeces = [x % my_length for x in range(current_position,current_position+input_length)]
    my_list[indeces] = np.flipud(my_list[indeces])
    current_position = (current_position + input_length + skip_size) % my_length
    skip_size +=1
    print(my_list)

print(my_list[0]*my_list[1])
    
#####################################################################

input_lengths = '34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'
my_length = 256
my_list = np.array(range(my_length))
end_seq = [17, 31, 73, 47, 23]

input_lengths_ascii = []
for c in input_lengths:
    input_lengths_ascii.append(ord(c))

for num in end_seq:
    input_lengths_ascii.append(num)

current_position = 0
skip_size = 0

for round in range(64):
    for input_length in input_lengths_ascii:
        indeces = [x % my_length for x in range(current_position,current_position+input_length)]
        my_list[indeces] = np.flipud(my_list[indeces])
        current_position = (current_position + input_length + skip_size) % my_length
        skip_size +=1


my_matrix = np.reshape(my_list, (16, 16))

def xor_of_array(my_array):
    '''Take xor for all consecutive elements of a 1-D array'''
    elem_xor = my_array[0]
    for elem in my_array[1:]:
        elem_xor = elem_xor ^ elem
    return elem_xor
           
xor_array = np.apply_along_axis(xor_of_array, 1, my_matrix)

print(''.join('{:02X}'.format(a) for a in xor_array))


