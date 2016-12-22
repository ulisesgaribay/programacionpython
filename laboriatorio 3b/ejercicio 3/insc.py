#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,2*math.pi,100)
x=np.sin(3*t)
y=np.sin(4*t)
plt.plot(t,x,linewidth=6,color='r',label='Funcion1')
plt.plot(t,y,linewidth=7,color='g',label='Funcion2')
plt.legend()
plt.title('Ejercicio 3.c)')
plt.xlabel('Dias')
plt.ylabel('Eventos')
plt.grid(True)
plt.show()
