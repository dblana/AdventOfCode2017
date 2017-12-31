# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:15:42 2017

@author: Dimitra
"""

#def foo():
#    print("Part 1")
#    a = 5
#    i = yield a
#    print(a+i)
#    yield
    
registerA = {}

instructions = []

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

with open('day18_input.txt') as f:
    for line in f:
        instructions += [line]
        line_parts = line.split()
        for part in line_parts[1:]:
            if not check_int(part) and part not in registerA:
                registerA[part] = 0
        
registerB = dict(registerA)
registerB['p'] = 1
         
queueA = []
queueB = []

         
def readA():   
    index = 0   

    while index<len(instructions):
        
        #print(index)
        
        line_parts = instructions[index].split()
        
        #print(line_parts[0])
        
        if line_parts[0] =='snd':
            queueA.append(registerA[line_parts[1]])
            #print(queueA)
            index +=1
        elif line_parts[0] == 'rcv':
            if len(queueB)==0:
                yield 
                if len(queueB)==0:
                    return 0
                else:
                    registerA[line_parts[1]] = queueB.pop(0)
            else:
                registerA[line_parts[1]] = queueB.pop(0)
            index +=1
        elif line_parts[0] == 'set':
            if line_parts[2] not in registerA:
                registerA[line_parts[1]] = int(line_parts[2])
            else:
                registerA[line_parts[1]] = registerA[line_parts[2]]
            index +=1
        elif line_parts[0] == 'add':
            if line_parts[2] not in registerA:
                registerA[line_parts[1]] += int(line_parts[2])
            else:
                registerA[line_parts[1]] += registerA[line_parts[2]]
            index +=1
        elif line_parts[0] == 'mul':
            if line_parts[2] not in registerA:
                registerA[line_parts[1]] *= int(line_parts[2])
            else:
                registerA[line_parts[1]] *= registerA[line_parts[2]]
            index +=1
        elif line_parts[0] == 'mod':
            if line_parts[2] not in registerA:
                registerA[line_parts[1]] = registerA[line_parts[1]] % int(line_parts[2])
            else:
                registerA[line_parts[1]] = registerA[line_parts[1]] % registerA[line_parts[2]]
            index +=1
        else:
            if line_parts[1] in registerA:
                value = registerA[line_parts[1]]
            else:
                value = int(line_parts[1])
            if value > 0:
                if line_parts[2] not in registerA:
                    index += int(line_parts[2])
                else:
                    index += registerA[line_parts[2]]
            else:
                index +=1
                
def readB():   
    sendB = 0
    index = 0 
    while index<len(instructions):
        #print(index)
        line_parts = instructions[index].split()
        #print(line_parts[0])
        if line_parts[0] =='snd':
            queueB.append(registerB[line_parts[1]])
            sendB +=1
            index +=1
        elif line_parts[0] == 'rcv':
            if len(queueA)==0:
                yield sendB
                if len(queueA)==0:
                    return sendB
                else:
                    registerB[line_parts[1]] = queueA.pop(0)
            else:
                registerB[line_parts[1]] = queueA.pop(0)
            index +=1
        elif line_parts[0] == 'set':
            if line_parts[2] not in registerB:
                registerB[line_parts[1]] = int(line_parts[2])
            else:
                registerB[line_parts[1]] = registerB[line_parts[2]]
            index +=1
        elif line_parts[0] == 'add':
            if line_parts[2] not in registerB:
                registerB[line_parts[1]] += int(line_parts[2])
            else:
                registerB[line_parts[1]] += registerB[line_parts[2]]
            index +=1
        elif line_parts[0] == 'mul':
            if line_parts[2] not in registerB:
                registerB[line_parts[1]] *= int(line_parts[2])
            else:
                registerB[line_parts[1]] *= registerB[line_parts[2]]
            index +=1
        elif line_parts[0] == 'mod':
            if line_parts[2] not in registerB:
                registerB[line_parts[1]] = registerB[line_parts[1]] % int(line_parts[2])
            else:
                registerB[line_parts[1]] = registerB[line_parts[1]] % registerB[line_parts[2]]
            index +=1
        else:
            if line_parts[1] in registerB:
                value = registerB[line_parts[1]]
            else:
                value = int(line_parts[1])
            if value > 0:
                if line_parts[2] not in registerB:
                    index += int(line_parts[2])
                else:
                    index += registerB[line_parts[2]]
            else:
                index +=1
                
r1 = readA()
r2 = readB()

while True:    
    print(str(next(r2)))
    next(r1)

r1.close()
r2.close()