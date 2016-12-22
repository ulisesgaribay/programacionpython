#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(-2*math.pi,2*math.pi,120)
x=t+2*np.sin(2*t)
y=t+2*np.cos(5*t)
plt.plot(t,x,linewidth=3,color='g',label='Funcion1')
plt.plot(t,y,linewidth=10,color='g',label='Funcion2')
plt.legend()
plt.title('Ejercicio 3.b')
plt.xlabel('Dias')
plt.ylabel('Eventos')
plt.grid(True)
plt.show()
