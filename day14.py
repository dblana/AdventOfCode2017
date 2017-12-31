# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 16:49:22 2017

@author: Dimitra
"""

import numpy as np

def xor_of_array(my_array):
    '''Take xor for all consecutive elements of a 1-D array'''
    elem_xor = my_array[0]
    for elem in my_array[1:]:
        elem_xor = elem_xor ^ elem
    return elem_xor

def knot_hash(input_lengths):
    '''Builts knot hash from Advent of Code Day 10
    '''
    
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
                   
    xor_array = np.apply_along_axis(xor_of_array, 1, my_matrix)
    
    hash_result = ''.join('{:02X}'.format(a) for a in xor_array)
    
    return hash_result

def count_ones_in_hash(hash_input):
    '''Counts how many 1 are in the binary representation of the output
    of the knot hash
    '''
    
    hex_hash_output = knot_hash(hash_input)
    
    binary_hash_output = ''
    for hexnum in hex_hash_output:
        binary_hash_output += bin(int(hexnum, 16))[2:].zfill(4)
    
    return binary_hash_output.count('1')

hash_input = 'vbqugkhl'
#hash_input = 'flqrgnkx'

#answer = 0
#for i in range(128):
#    input_hash = hash_input+'-'+str(i)
#    #print(input_hash)
#    answer += count_ones_in_hash(input_hash)
#
#print(answer)


def get_all_squares(hash_input):
    '''Saves output of knot hashe in a string
    '''
    
    hex_hash_output = knot_hash(hash_input)
    
    binary_hash_output = ''
    for hexnum in hex_hash_output:
        binary_hash_output += bin(int(hexnum, 16))[2:].zfill(4)
    
    return binary_hash_output


hash_list = []
for i in range(128):
    input_hash = hash_input+'-'+str(i)
    #print(input_hash)
    hash_list.append(get_all_squares(input_hash))
    

def check_square(pos,hash_list,current_set):
    '''Checks if current square is 1 or 0. If it is 0, it returns
    If it is 1, it checks whether it is already in the current set.
    If it is, it returns. If it is not, it adds it to the current set,
    finds all adjacent squares and calls itself.'''
    
    if hash_list[pos[0]][pos[1]] == '0':
        return current_set
    else:
        if pos in current_set:
            return current_set
        else:
            # add square and check all adjacent squares
            current_set.append(pos.copy())
            if pos[0]<len(hash_list)-1:
                pos[0]+=1
                current_set = check_square(pos,hash_list,current_set)
                pos[0]-=1
                
            if pos[1]<len(hash_list)-1:
                pos[1]+=1
                current_set = check_square(pos,hash_list,current_set)
                pos[1]-=1
                
            if pos[0]>0:
                pos[0]-=1
                current_set = check_square(pos,hash_list,current_set)
                pos[0]+=1
                
            if pos[1]>0:
                pos[1]-=1
                current_set = check_square(pos,hash_list,current_set)
                pos[1]+=1
                
            return current_set

#hash_list = ['1101','0111','0000','1000']
all_squares = []

start = [0,0]   
counter = 0

for i in range(len(hash_list)):
    for j in range(len(hash_list)):
        pos = [i,j]
        if pos in all_squares:
            continue
        if hash_list[pos[0]][pos[1]] == '0':
            continue
        current_set = check_square(pos,hash_list,[])
        all_squares += current_set
        counter+=1

print(counter)
print(len(all_squares))