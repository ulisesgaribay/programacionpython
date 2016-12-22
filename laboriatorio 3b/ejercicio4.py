#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0.0,2,0.01)
y1=np.sin(2*np.pi*x)
y2=1.2*np.sin(4*np.pi*x)

plt.subplot(3,1,1)
plt.fill_between(x,0,y1)
plt.ylabel('between y1 and 0')

plt.subplot(3,1,2)
plt.fill_between(x,y1,1)
plt.ylabel('between y1 and y2')

plt.subplot(3,1,3)
plt.fill_between(x,y1,y2)
plt.ylabel('between yi and y2')
plt.xlabel('x')

plt.show()
