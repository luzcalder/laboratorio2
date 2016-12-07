#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#luz maria calderon aguilera
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,4*math.pi,100)
s=np.cos(2*x)+np.sin(3*x)
v=-2*np.sin(2*x)+3*np.cos(3*x)
plt.plot(x,s, linewidth=3,color='r',label='parabola')
plt.plot(x,v, linewidth=3,color='b',label='elipse')
plt.legend()
plt.title('s,v')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.prig')
