#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math

x=np.linspace(0,2,120)

y=x*math.e**(-3*x)
b=math.e**(-3*x)
plt.plot(x,y,linewidth=4,color='g',label='f(x)')
plt.plot(x,b,linewidth=6,color='r',label='g(x)')
plt.legend()
plt.title('Ejercicio 2.b')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
