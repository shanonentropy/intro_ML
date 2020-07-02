# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:14:21 2019

@author: zee-erika
"""

''' practice coding with matplotlib'''
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

y=np.random.randn(500000)
x=np.arange(0,500000)
z=x*y*0.01
#generate a XY plot

plt.plot(x,y)
plt.title('XY plot')
plt.show('Figure 1')

#create a stockplot

plt.stackplot(x,y,z, colors=['b','r'], linewidth=[1])
plt.xlabel('x')
plt.ylabel('y')
plt.show('Figure 1b')

#generate a Histogram

plt.hist(y,100)
plt.title('Histogram plot')
plt.show('Figure 2')

#pie chart
legpress=[45,90,135,180,210,280]
weeks=['week 1','week 2','week 3','week 4','week 5', 'week 6']
plt.pie(legpress, labels=weeks, colors=['m', 'c','r','k','g','b'])

#open a pandas file
import pandas as pd
df=pd.read_csv('pandas_practice.csv')
a=df['A']
b=df['B']
plt.plot(a[::5], b[::5],'o')
plt.plot(a,b,'r+')
plt.legend('b_skip5')
plt.legend('all_b')
plt.show('Figure 3a')
plt.hist(df['C'],3)
plt.legend('C')
plt.show('Figure 3b')

#bar plot

countries=['Pakistan', 'India','Australia','West Indies', 'England']
wins=[1,2,3,2,0.5]
plt.bar(countries,wins)
plt.show('Figure 4')
#box plot

plt.boxplot(wins)
plt.show('Figure 5')

#scatter plot

plt.scatter(df['A'],df['B'])
plt.show('Figure 5')  

#create plot with regression using seaborn
import seaborn as sns
ax = sns.regplot(x=df['A'],y=df['B'], data =df)
plt.show()


