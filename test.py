import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import step, show 
from matplotlib.animation import FuncAnimation
import random
from itertools import count

x1 = []
y1 = []
index = count()
def animate(i):
    x1.append(next(index))
    y1.append(random.randint(0,1))
    plt.cla()
    step(x1, y1)
    
    
    
ani = FuncAnimation(plt.gcf(),animate,interval = 1000)
plt.show()