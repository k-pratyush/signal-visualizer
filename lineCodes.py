from itertools import count
import numpy as np
from helpers import ADC, lengthNormalizer, binaryAdder

def initialize(input_array):
    return binaryAdder(lengthNormalizer(ADC(input_array)))

def unipolar(arr):
    bit_string = initialize(arr)
    l = []
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            l.append(0)
        else:
            l.append(1)
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y

def NRZ_L(arr):
    bit_string = initialize(arr)
    l = []
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            l.append((1))
        else:
            l.append(-1)
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y

def NRZ_I(arr):
    bit_string = initialize(arr)
    l = []
    counter=0
    l.append(int(bit_string[1]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            if (counter % 2) == 0:
               l.append((1))
            else:
               l.append((-1))
        else:
            counter += 1
            if (counter % 2) == 0:
               l.append((1))
            else:
               l.append((-1)) 
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y 

def RZ(arr):
    bit_string = initialize(arr)
    l = []
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            l.append((0))
            l.append((0))
        else:
            l.append(1)
            l.append((0))
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y

def bipolar(arr):
    bit_string = initialize(arr)
    l = []
    counter=0
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            l.append((0))
        else:
            counter += 1
            if (counter % 2) == 0:
               l.append((-1))
            else:
               l.append((1)) 
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y

def manchester(arr):
    bit_string = initialize(arr)
    l = []
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            l.append((1))
            l.append((-1))
        else:
            l.append(-1)
            l.append((1))
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y       

def differential_manchester(arr):
    bit_string = initialize(arr)
    l = []
    counter=0    
    l.append(int(bit_string[0]))
    for i in range(0,len(bit_string)):
        if bit_string[i] == '0':
            if (counter % 2) == 0:
                l.append((-1))
                l.append((1))
            else:
               l.append((1))
               l.append((-1))
        else:
            counter += 1
            if (counter % 2) == 0:
               l.append((-1))
               l.append((1))
            else:
               l.append((1))
               l.append((-1)) 
    x = np.arange(0, len(l))
    y = np.array(l)
    return x,y
