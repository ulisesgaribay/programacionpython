#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

k=np.linspace(0,2*np.pi,0.015)
r=-250*np.sin(5*k)*np.cos(4*k)
s=k+np.sin(r/100)
x=320+r*np.cos(s)
y=-240-r*np.sin(s)
plt.plot(x,y,linewidth=10,color='g',label='Grafica')
plt.legend()
plt.title('Ejercicio 6)')
plt.xlabel('Tiempo')
plt.ylabel('Dias')
plt.fill_between(x,y,color='r')
plt.axis('equal')
plt.axis('off')
plt.grid(True)
plt.show()
