#!usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

t=np.linspace(0,2*math.pi,99)
x=np.cos(t)**3
y=np.sin(t)**3
plt.plot(t,x,linewidth=5,color='r',label='Funcion1')
plt.plot(t,y,linewidth=5,color='k',label='Funcion2')
plt.legend()
plt.title('Ejercicio 3.a)')
plt.xlabel('Dias')
plt.ylabel('Eventos')
plt.grid(True)
plt.show()
