#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#luz maria calderon aguilera
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,2*math.pi,100)
x=np.cos(t)*np.cos(t)*np.cos(t)
y=np.sin(t)*np.sin(t)*np.sin(t)
plt.plot(t,x, linewidth=3,color='r',label='parabola')
plt.plot(t,y, linewidth=3,color='b',label='elipse')
plt.legend()
plt.title('$cos^3,sen^3$')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.prig')
