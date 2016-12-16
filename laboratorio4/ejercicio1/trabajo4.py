# _*_ coding: utf-8 _*_
#1-b
#luz maria calderon aguilera
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(-1,5,100)
g=t*np.e**-2*t
plt.plot(t,g, linewidth=3,color='g',label='grafica')
plt.legend()
plt.title('$te^-2t$')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.png')
