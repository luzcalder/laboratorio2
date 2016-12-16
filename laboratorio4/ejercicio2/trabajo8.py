#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#luz maria calderon aguilera
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,4*math.pi,100)
f=np.sin(3*t)*np.cos(2*t)
g=.5*np.cos(2*t)+2.5*np.cos(5*t)
plt.plot(t,f, linewidth=3,color='r',label='linea1')
plt.plot(t,g, linewidth=3,color='b',label='linea2')
plt.legend()
plt.title('f,g')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.png')
