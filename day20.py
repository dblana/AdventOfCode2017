# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:32:57 2017

@author: Dimitra
"""
import re
import pandas as pd

data=[]

#line = 'p=<1500,413,-535>, v=<-119,22,36>, a=<-5,-12,3>'
#numbers = [int(s) for s in re.findall(r'-*\d+',line)]

with open('day20_input.txt') as f:
    for line in f:
        data.append([int(s) for s in re.findall(r'-*\d+',line)])

df = pd.DataFrame(data,columns=['px','py','pz','vx','vy','vz','ax','ay','az'])
df['dist_from_zero'] = abs(df['px']) + abs(df['py']) + abs(df['pz'])

for i in range(1000):
    df['vx']  += df['ax']
    df['vy']  += df['ay']
    df['vz']  += df['az']
    df['px'] += df['vx']
    df['py'] += df['vy']
    df['pz'] += df['vz']
    
df['dist_from_zero1000'] = abs(df['px']) + abs(df['py']) + abs(df['pz'])

print(df.loc[df['dist_from_zero'].idxmin()])
print(df.loc[df['dist_from_zero1000'].idxmin()])

################################################

df = pd.DataFrame(data,columns=['px','py','pz','vx','vy','vz','ax','ay','az'])
df['location'] = df['px'].apply(str) + df['py'].apply(str) + df['pz'].apply(str)
values = df['location'].value_counts().to_frame()
values = values[values.location>1]
df = df[~df.location.isin(values.index)]

for i in range(1000):
    df['vx']  += df['ax']
    df['vy']  += df['ay']
    df['vz']  += df['az']
    df['px'] += df['vx']
    df['py'] += df['vy']
    df['pz'] += df['vz']
    df['location'] = df['px'].apply(str) + df['py'].apply(str) + df['pz'].apply(str)
    values = df['location'].value_counts().to_frame()
    values = values[values.location>1]
    df = df[~df.location.isin(values.index)]


