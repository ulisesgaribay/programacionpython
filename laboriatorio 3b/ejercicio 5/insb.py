#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

k=np.linspace(0,2*np.pi,100)
r=2-2*np.sin(k)+np.sin(k)*(np.sqrt(np.absolute(np.cos(k))))/(np.sin(k)+1.4)
x=r*np.cos(k)
y=r*np.sin(k)
plt.plot(x,y,linewidth=10,color='r',label='Corazon')
plt.legend()
plt.title('Ejercicio 5b)')
plt.xlabel('Momentos')
plt.ylabel('Dias')
plt.fill_between(x,y,color='r')
plt.grid(True)
plt.show()
