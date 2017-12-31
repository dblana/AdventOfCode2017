# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:48:08 2017

@author: Dimitra
"""
import time

step = 367
#ninsert = 50000000
ninsert = 2017

#step = 3
#ninsert = 10

cbuffer = [0]
current_pos = 0
num_after_zero = 0

start_time = time.time()

for i in range(ninsert):
    current_pos += step
    current_pos = (current_pos % len(cbuffer))+1
    cbuffer.insert(current_pos,i+1)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))

print(cbuffer[current_pos])

##########################################

step = 367
ninsert = 50000000
#ninsert = 5000

#step = 3
#ninsert = 10

len_buffer=1
current_pos = 0

start_time = time.time()

for i in range(ninsert):
    current_pos += step
    current_pos = (current_pos % len_buffer)+1
    len_buffer +=1
    if current_pos==1:
        print(i+1)

end_time = time.time()
print("Elapsed time was %g seconds" % (end_time - start_time))