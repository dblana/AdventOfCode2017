# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:06:36 2017

@author: Dimitra
"""

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()
        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data


############# Q1 ##############################################

valid_pass=0

# Open a connection to the file
with open("day4_input.txt") as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.rstrip('\n').split(' ')
        
        # Initialize an empty dictionary: counts_dict
        counts_dict = {}
        invalid=0

        for word in row:            
            if word in counts_dict.keys():
                invalid = 1
            else:
                counts_dict[word] = 1
        if invalid==0:
            valid_pass +=1

print(valid_pass)


############# Q2 ##############################################

valid_pass=0

# Open a connection to the file
with open("day4_input.txt") as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.rstrip('\n').split(' ')
        
        # Initialize an empty dictionary: counts_dict
        counts_dict = {}
        invalid=0

        for unsorted_word in row:    
            word = ''.join(sorted(unsorted_word))
            if word in counts_dict.keys():
                invalid = 1
            else:
                counts_dict[word] = 1
        if invalid==0:
            valid_pass +=1

print(valid_pass)

