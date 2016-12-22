#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1,5,100)
y = 2*(x**2)-8*x-11
plt.plot(x,y,linewidth=4,color='r',label='g(x)=2x^2-8x-11' )
plt.legend()
plt.title('grafica b')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
