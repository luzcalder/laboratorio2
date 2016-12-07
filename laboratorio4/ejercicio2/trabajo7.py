#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#luz maria calderon aguilera
#2-b
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(0,2,100)
f=x*np.e**-3*x
g=np.e**-3*x*(1-3*x)
plt.plot(x,f, linewidth=3,color='r',label='linea1')
plt.plot(x,g, linewidth=3,color='b',label='linea2')
plt.legend()
plt.title('f,g')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.prig')
