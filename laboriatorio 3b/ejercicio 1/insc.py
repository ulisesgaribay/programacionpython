#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import math
t = np.linspace(-1,5,600)
y = t*(math.e**(-2*t))
plt.plot(t,y,linewidth=10,color='y',label='f(t)=te^-2t' )
plt.legend()
plt.title('grafica c')
plt.xlabel('Tiempo')
plt.ylabel('Metros')
plt.grid(True)
plt.show()
