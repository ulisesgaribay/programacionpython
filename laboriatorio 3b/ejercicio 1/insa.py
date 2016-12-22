#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-6,2,100)
y = 5-4*x-x**2
plt.plot(x,y,linewidth=4,color='g',label='f(x)=5-4x-x^2' )
plt.legend()
plt.title('grafica a')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
