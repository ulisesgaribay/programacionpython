#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import math
t = np.linspace(0,24,500)
y = (math.e**(-0.1*t))*np.sin(2*t)
plt.plot(t,y,linewidth=2,color='b',label='h(t)= (e^-0.1t)sen(2t)')
plt.legend()
plt.title('grafica d')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
