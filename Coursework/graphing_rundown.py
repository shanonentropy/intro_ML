# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:27:33 2019

@author: zee-erika
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,100,2)
y=x*2
z=np.cos(x)-10


### make simple XY plot 
plt.subplot(121)
plt.plot(x,y, 'bD', ms=5, mfc='none', label='XY')
plt.xlabel('X-axis', size=18)
plt.ylabel('Y-axis', size =18)
plt.title('graph', size=18)
plt.tick_params(axis='both', labelsize=15, width=3, length=5)
plt.legend(loc='best')

plt.subplot(122)
plt.plot(x,z, 'kx-.', ms=5, mfc='none', label='XZ')
plt.xlabel('X-axis', size=18)
plt.ylabel('Z-axis', size =18)
plt.title('graph', size=18)
plt.tick_params(axis='both', labelsize=15, width=3, length=5)
plt.tight_layout()
plt.legend(loc='lower center')
plt.show()

### make a Histogram
plt.hist(z, bins=5)
plt.show()

### pie char
expenditure=[200,300,100,500]
week=['week 1','week 2', 'week 3', 'week 4']
plt.pie(expenditure, labels=week)
plt.show()

### bar graph

plt.bar(week, expenditure, color='lightblue', edgecolor=['blue', 'blue', 'blue','blue'])
plt.show()

### box plot

plt.boxplot(y)
#plt.boxplot(z*100)
plt.show()

### stackplot
plt.stackplot(x, y*0.5,z*10,z*50)
plt.show()
### scatter plot

plt.scatter(x,y,c=z,cmap='copper')
plt.show()
### color map plot
a=np.array(10*(x,z))
#a=np.stack((a,a))
plt.imshow(a, interpolation='none', cmap='summer')
plt.show()

