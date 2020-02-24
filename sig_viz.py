import matplotlib.pyplot as plt
from matplotlib.pyplot import step, show 
from matplotlib.animation import FuncAnimation
import random
from itertools import count
from scipy.io import wavfile as wav
from scipy.io.wavfile import read
from scipy.fftpack import fft
import numpy as np
import wave
import sys

rate, data = wav.read('Recording.wav')
x1 = np.arange(0, 100, 0.1)
y1 = np.sin(x1)
#plt.plot(x1,y1)
#plt.plot(data)
#plt.show()
spf = wave.open('Recording.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.frombuffer(signal, 'Int16')

fs = spf.getframerate()
Time=np.linspace(0, len(signal)/fs, num=len(signal))

#plt.figure(1)
#plt.title('Signal Wave...')
#plt.plot(Time,signal)
#plt.show()
print(len(data))


input_data = read("Recording.wav")
audio = input_data[1]

#plt.plot(audio[0:400])

#plt.ylabel("Amplitude")
#plt.xlabel("Time (samples)")
 # set the title
#plt.title("Audio sample")
# display the plot
#plt.show()
def lengthNormalizer(numpy_array):
    output_array = []
    for i in range(0, len(numpy_array)):
        output_array.append(format(numpy_array[i], '015d'))
    return output_array

# Converts array of normalized binary numbers into a long string\n",
def binaryAdder(ys_length_normalized):
    result = ""
    for bit in ys_length_normalized:
        result += bit
    return result

def ADC(numpy_array):
    numpy_array = numpy_array.astype('int64')
    for i in range(0, len(numpy_array)):
        #print(numpy_array[i])
        numpy_array[i] = bin(numpy_array[i]).replace('0b', '')
    return numpy_array
    

x_axis = []
y_axis = []
for x, y in audio:
    y_axis.append(y)

x_axis = np.arange(0, len(y_axis))
ys = np.array(y_axis)
xl = x_axis[0:1024]
yl = ys[0:1024]
print(ys.round())
#plt.bar(x_axis[0:1024], ys[0:1024], bottom=0, width=0.2)
#plt.show()



yl = ADC(yl)
yl = lengthNormalizer(yl)
yl = binaryAdder(yl)

def unipolar(b):
    l = []
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
            l.append(0)
        else:
            l.append(1)
        x = np.arange(0, len(l))
        y = np.array(l)
    #step(x, y)
    #plt.show()
    return x,y

def NRZ_L(b):
    l = []
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
            l.append((1))
        else:
            l.append(-1)
        x = np.arange(0, len(l))
        y = np.array(l)
    #step(x, y)
    #plt.show()
    return x,y

def NRZ_I(b):
    l = []
    counter=0
    l.append(int(b[1]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
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
    #step(x, y)
    #plt.show()
    return x,y 

def RZ(b):
    l = []
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
            l.append((0))
            l.append((0))
        else:
            l.append(1)
            l.append((0))
        x = np.arange(0, len(l))
        y = np.array(l)
    #step(x, y)
    #plt.show()
    return x,y


def bipolar(b):
    l = []
    counter=0
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
            l.append((0))
    
        else:
            counter += 1
            if (counter % 2) == 0:
               l.append((-1))
            else:
               l.append((1)) 
        x = np.arange(0, len(l))
        y = np.array(l)
    #step(x, y)
    #plt.show()
    return x,y 

def manchester(b):
    l = []
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):
            l.append((1))
            l.append((-1))
        else:
            l.append(-1)
            l.append((1))
        x = np.arange(0, len(l))
        y = np.array(l)
    #step(x, y)
    #plt.show()
    return x,y       

def diffrential_manchester(b):
    l = []
    counter=0    
    l.append(int(b[0]))
    for i in range(0,len(b)):
        if(b[i]=='0'):    
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
    #step(x, y)
    #plt.show()
    return x,y 

x2,y2 = unipolar(yl)
x3,y3 = NRZ_I(yl)
x4,y4 = diffrential_manchester(yl)
x4 = list(x4)
print(len(x4))
y4 = list(y4[1900:])
y3 = list(y3[950:])
y2 = list(y2[950:])
y2 = iter(y2)
y3 = iter(y3)
y4 = iter(y4)
x4 = iter(x4)
index = count()
x11 =[]
y11=[]
y12 =[]
y13=[]
x44 = np.arange(0,1000,0.5)
x44 = list(x44)
x44 = iter(x44)
x12 =[]
#k = [i for i in range(0,1000)]
#k = iter(k)
fig,a =  plt.subplots(3,1,sharex='col',figsize=(20, 10))
def animate(i):
    x11.append(next(index))
    x12.append(next(x44))
    y11.append(next(y2))
    y12.append(next(y3))
    y13.append(next(y4))
    a[2].step(x12 , y13,'r')
    y13.append(next(y4))
    x12.append(next(x44))
    #plt.figure(figsize=(20,10))
    plt.cla()
    if(x11[-1]<20):
        plt.xlim((0 ,20 ))
    else:
        plt.xlim((x11[-20] ,+x11[-1] ))
    #plt.ylim(-1,1)
    a[0].set_ylim([-1,1.1])
    a[0].step(x11,y11,'g')
    a[0].set_title('UNIPOLAR')
    a[1].step(x11, y12,'b')
    a[1].set_title('POLAR')
    a[2].step(x12 , y13,'r')
    a[2].set_title('RZ')
    
ani = FuncAnimation(fig,animate,interval = 100)



#plt.title("ani")
plt.show()

#print(ys)
#print(type(y2))
