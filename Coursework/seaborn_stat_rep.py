# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 21:31:07 2019

@author: zee-erika
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style(style='darkgrid')

a=np.linspace(0,100,100)
b=np.random.randint(0,100,100)
c=np.cos(a)+np.sin(b)

####### scatter plot 
df=pd.read_csv('multivar_reg.csv')
df.sort_values('t')
df.dropna()
#sns.relplot(x='t', y='ft', data=df)
#sns.relplot(x='t', y='fts', data=df, hue='size')
"""

####### line plot

#data plotted as a line with no aggregation
sns.relplot(x='t', y='ft', kind='line', ci='sd',estimator=None, data=df)
#data plotted with aggregation
sns.relplot(x='t', y='ft', kind='line', data=df)
#note when multiple measurements are present seaborn puts up an uncertainty shadow
#equal to a 95% confidence interval
#we can use keyword ci='sd' to use a standard deviation instead of confidence interval
sns.relplot(x='t', y='ft', kind='line', ci='sd',data=df)
plt.show()


sns.set(color_codes=True)

### univariate distribution

sns.distplot(b, hist=False)
plt.show()
#rug plot
sns.distplot(b, rug=True, bins=5)
plt.show()
#density plot
sns.kdeplot(b, shade=True)
####you can specify the bw of gaussians used to fit the data to calc density plot
sns.kdeplot(b, bw=10)
################################ bivariates ---see joint plots
########### regression plots)

sns.regplot(x=a, y=b, robust=True)
plt.show()
sns.lmplot(x='t', y='ft', x_estimator=np.mean, data=df) #only works with panda series
plt.show()
"""

sns.lmplot(x='t', y='ft', data=df, order=3, fit_reg=True, ci=95)
plt.show()
sns.residplot(x='t', y='ft', order=3, data=df)
plt.show()
plt.plot(figsize=(5,6))
sns.lmplot(x='t', y='fts', order=2,data=df)