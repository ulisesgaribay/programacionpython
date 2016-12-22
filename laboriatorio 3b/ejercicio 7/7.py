#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

k=np.linspace(0,4*np.pi,0.04)
r=150+100*np.sin(4.5*k)
s=k-(np.cos(10*k))/(10)
x=320+r*np.cos(s)
y=-240-r*np.sin(s)
plt.plot(x,y,linewidth=10,color='k',label='Grafica')
plt.legend()
plt.title('Ejercicio 7)')
plt.xlabel('Tiempo')
plt.ylabel('Dias')
plt.fill_between(x,y,color='r')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
