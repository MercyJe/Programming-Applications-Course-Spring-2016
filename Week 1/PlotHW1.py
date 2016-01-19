#import numpy and matlibplots module
import numpy as np
import matplotlib.pyplot as plt

#generate array of x values from 0 to 6pi
xvalues = np.linspace(0, 6*np.pi, 100, endpoint=False)

#calculate y values for sine wave
ysin = np.sin(xvalues)
#calculatfor cosine wave y values 
ycos = np.cos(xvalues)

#plot x and y values for both functions 
#set dashed line for sine wave and solide line for cosine wave
plt.plot(xvalues, ysin, '--b', linewidth=1.5, label = 'sine')
plt.plot(xvalues, ycos, '-g',linewidth=1.5, label = 'cosine')
plt.grid()
plt.xlabel('x')
plt.ylabel('sine and cosine')
plt.title('Two Trigonometric graphs on one page')

#add legend
plt.legend( loc='upper right')
plt.show()

#leave comment here with your information
#Name: Mercy J. Daniel Aguebor
#Date: 1 - 18 - 2016

