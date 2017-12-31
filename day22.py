# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 08:12:13 2017

@author: Dimitra
"""

nodes = []
x = -1
y = -1


with open('day22_input.txt') as f:
    for line in f:
        y +=1
        x = -1
        for c in line:
            x +=1
            if c=='#':
                nodes.append((y,x))

sizex = x+1
sizey = y+1

vel = (-1,0)
pos = (int(sizex/2),int(sizey/2))
cause_infection = 0

def turn_right(vel):
    '''return new velocity tuple, at 90 degrees to the right'''
    if vel[0]==1:
        return (0,-1)
    elif vel[0]==-1:
        return (0,1)
    elif vel[1]==1:
        return (1,0)
    else:
        return (-1,0)

def turn_left(vel):
    '''return new velocity tuple, at 90 degrees to the left'''
    if vel[0]==1:
        return (0,1)
    elif vel[0]==-1:
        return (0,-1)
    elif vel[1]==1:
        return (-1,0)
    else:
        return (1,0)

def reverse(vel):
    '''return new velocity tuple, at opposite direction'''
    if vel[0]==1:
        return (-1,0)
    elif vel[0]==-1:
        return (1,0)
    elif vel[1]==1:
        return (0,-1)
    else:
        return (0,1)

def burst(pos,vel,nodes,cause_infection):
    '''performs three steps of activity'''
    if pos in nodes:
        new_vel = turn_right(vel)
        nodes.remove(pos)
    else:
        new_vel = turn_left(vel)
        nodes.append(pos)
        cause_infection +=1

    new_pos = (pos[0] + new_vel[0],pos[1] + new_vel[1])
    return new_pos, new_vel, nodes, cause_infection

for i in range(10000):
    (pos,vel,nodes,cause_infection) = burst(pos,vel,nodes,cause_infection)

print(cause_infection)

def evolved_burst(pos,vel,nodes,cause_infection):
    '''performs three steps of activity'''
    if pos in nodes:
        new_vel = turn_right(vel)
        nodes.remove(pos)
    else:
        new_vel = turn_left(vel)
        nodes.append(pos)
        cause_infection +=1

    new_pos = (pos[0] + new_vel[0],pos[1] + new_vel[1])
    return new_pos, new_vel, nodes, cause_infection
