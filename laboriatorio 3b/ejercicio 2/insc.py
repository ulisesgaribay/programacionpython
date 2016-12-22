#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,4*math.pi,90)

f=np.sin(3*t)*np.cos(2*t)
g=1/2*np.cos(t)+5/2*np.cos(5*t)
plt.plot(t,f,linewidth=4,color='k',label='f(t)')
plt.plot(t,g,linewidth=6,color='g',label='g(t)')
plt.legend()
plt.title('Ejercicio 2.c')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
