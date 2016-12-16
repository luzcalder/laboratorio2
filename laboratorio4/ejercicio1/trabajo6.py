# _*_ coding: utf-8 _*_
#1-b
#luz maria claderon aguilera
import matplotlib.pyplot as plt
import numpy as np
import math
t=np.linspace(0,24,100)
g=math.e**-0.1*t*(np.sin*(2*t))
plt.plot(t,g, linewidth=3,color='g',label='grafica')
plt.legend()
plt.title('$e^-0.1t(sen(2t))$')
plt.xlabel('algo')
plt.ylabel('una funcion de algo')
plt.show()
plt.savefig('grafica.png')
