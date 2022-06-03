#if matplotlib is not installed, use command "pip install matplotlib"
#importing modules

import numpy as np
import matplotlib.pyplot as plt

#Plotting multiple bars on 2 datasets

x1 = [2,4,6,8,10]
y1= [6,7,8,2,4]
x2= [1,3,5,7,9]
y2= [7,8,2,4,2]
plt.bar(x1,y1,label='data1',color='red')
plt.bar(x2,y2,label='data2',color='blue')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plotting multiple bars')
plt.legend()
plt.show()
