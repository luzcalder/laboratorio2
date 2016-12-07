#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#luz maria calderon aguilera
#1-b
import matplotlib.pyplot as plt
import numpy as np
import math
x=np.linspace(-1,5,100)
g=2*x**2-8*x-11
plt.plot(g,x, linewidth=3,color='b',label='grafica')
plt.legend()
plt.title('$2x^2-8x-11$')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.prig')
