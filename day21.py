# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:04:09 2017

@author: Dimitra
"""

# line = '#../.../... => ####/####/.###/####'
rules = {}

with open('day21_input.txt') as f:
    for line in f:
        pre,post = line.split(' => ')
        rules[pre] = post

pattern = '.#./..#/###'
#pattern = '##./..#/###'

def gen_rotations(pt):
    '''generate three clockwise rotations'''
    parts = pt.split('/')
    plen = len(parts)
    newparts = []
    for i in range(3):
        rotparts = [[parts[row][col] for row in range(plen-1,-1,-1)] for col in range(plen)]
        parts = [''.join(part) for part in rotparts]
        newparts.append('/'.join(parts))
    return newparts
    
def gen_flips_rotations(pt):
    '''generate all possible rotated and flipped versions
       of a given pattern'''    
    # flip vertically
    all_pts = [pt]
    all_pts.append('/'.join(pt.split('/')[::-1]))
    # flip horizontally
    parts = pt.split('/')
    rev_parts = [part[::-1] for part in parts]
    all_pts.append('/'.join(rev_parts))
    # rotate
    for i in range(3):
        all_pts += gen_rotations(all_pts[i])
    return list(set(all_pts))

def gen_output(pt,rulebook):
    '''find pattern pt in rulebook and return the output'''
    patterns = gen_flips_rotations(pt)
    for (rule,output) in rulebook.items():
        if rule in patterns:
             return output
    print("Pattern not found")
    print(pt)
    return -1

def make_art(pt,rulebook):
    '''make art with a pattern and a rulebook'''
    parts = pt.split('/')
    if len(parts)>3:
        if len(parts) % 2 == 0:
            size = 2
        else:
            size = 3
            
        all_out_parts = []
        nsize = size+1
        for i in range(int(len(parts)/size)*nsize):
            all_out_parts.append([])
            
        for i in range(int(len(parts)/size)):
            for j in range(int(len(parts)/size)):
                #print('/'.join([parts[index][j*size:(j+1)*size] for index in range(i*size,(i+1)*size)]))
                out = make_art('/'.join([parts[index][j*size:(j+1)*size] for index in range(i*size,(i+1)*size)]),rules)
                #print(out)
                out_parts = out.rstrip().split('/')
                for index in range(nsize):
                    all_out_parts[i*nsize+index].append(out_parts[index])
                    #print(all_out_parts)
        
        return '/'.join([''.join(row) for row in all_out_parts])                      

    else:
        return gen_output(pt,rulebook)


for i in range(18):
    print(i)
    pattern = make_art(pattern,rules)     
    print(pattern.count('#'))
    
    
    
    