# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:05:24 2017

@author: Dimitra
"""

grid=[]

with open('day19_input.txt') as f:
    for line in f:
        grid.append(line)

all_letters = [chr(65+i) for i in range(26)]
my_letters = []

x = grid[0].find('|')
y = 0
dx = 0
dy = 1
clue = '|'
steps = 0

while True:
    steps +=1
    x += dx
    y += dy
#    while grid[y][x] == clue:
#            steps +=1
#            x += dx
#            y += dy
    if grid[y][x] in all_letters:
        my_letters.append(grid[y][x])
    elif grid[y][x] == '+':
        if dy != 0:
            dy = 0
            clue = '-'
            if x==0:
                dx = 1
            elif x==len(grid[y]):
                dx = -1
            else:
                if grid[y][x+1] != ' ':
                    dx = 1
                else:
                    dx = -1
        else:
            dx = 0
            clue = '|'
            if y==0:
                dy = 1
            elif y==len(grid[x]):
                dy = -1
            else:
                if grid[y+1][x] != ' ':
                    dy = 1
                else:
                    dy = -1         
    elif grid[y][x] == ' ':
        break

print(''.join(my_letters))
        
         