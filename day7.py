# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:08:32 2017

@author: Dimitra
"""
import re

left_str = []
right_list =[]

#line = 'jfmuzo (164) -> istoj, jyzrmnp'

with open('day7_input.txt') as f:
    for line in f:
        if '->' in line:           
            bparts = re.split('\(.*>', line)
            left_str.append(bparts[0].strip())
            right_list.append(bparts[1].strip().split(', '))

flat_list = [item for sublist in right_list for item in sublist]

for istr in left_str:
    if istr not in flat_list:
        root_disc = istr
        print(root_disc)

###########################################

left_str = []
right_list =[]
nums_list = []

#line = 'jfmuzo (164) -> istoj, jyzrmnp'

with open('day7_input.txt') as f:
    for line in f:
        num = re.findall('\d+', line)
        nums_list.append(int(num[0]))
        if '->' in line:           
            bparts = re.split('\(.*>', line)
            left_str.append(bparts[0].strip())
            right_list.append(bparts[1].strip().split(', '))
        else:
            bparts = re.split('\(', line)
            left_str.append(bparts[0].strip())
            right_list.append([])

alldiscs = {}
for disc in left_str:
    disc_index = left_str.index(disc)
    alldiscs[disc] = [nums_list[disc_index], nums_list[disc_index], right_list[disc_index]]
    

def update_disc_weight(one_disc,all_discs):
    '''Updates the weight of a disc by adding the weight of the stack above it
    '''
    weight = all_discs[one_disc][1]
    # Find discs on this disc's stack        
    for disc in all_discs[one_disc][2]:
        if len(all_discs[disc][2])==0:
            weight += all_discs[disc][1]
        else:
            weight += update_disc_weight(disc,all_discs)
    all_discs[one_disc][1] = weight
    return weight    

update_disc_weight(root_disc,alldiscs)


def check_disc_weight(one_disc,all_discs,correction):
    '''Checks the weight of the disc's stack
    If it is balanced, it calculates the new weight of the disc+stack and saves it
    If not, it finds which disc has the wrong weight, and what the weight should be
    '''
    # Find discs on this disc's stack
    disc_weights = [all_discs[disc][1] for disc in all_discs[one_disc][2]]
    print(disc_weights)
    if disc_weights.count(disc_weights[0]) != len(disc_weights):
        wrong_weight = next(disc for disc in disc_weights if disc_weights.count(disc)!= len(disc_weights)-1)
        i = disc_weights.index(wrong_weight)
        if i != 0:
            correction = disc_weights[0] - wrong_weight
        else:
            correction = disc_weights[-1] - wrong_weight        
        check_disc_weight(all_discs[one_disc][2][i],all_discs,correction)
    else:
        print(all_discs[one_disc][0] + correction)
        

check_disc_weight(root_disc,alldiscs,0)