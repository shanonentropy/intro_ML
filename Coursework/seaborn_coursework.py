# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:35:52 2019

@author: zee-erika
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

x=np.arange(0,100,2)
y=x*2
z=np.cos(x)-10

### take data from pandas and do your magic
df=pd.read_csv('multivar_reg.csv')
#plot as a scatter plot
sns.jointplot(x='t', y='ft', data=df, color='purple', kind='scatter')
#w/reg line
sns.jointplot(x=y,y=z, kind='reg').set_axis_labels(xlabel='x-axis', ylabel='z-axis')
#w/residuals
sns.jointplot(x=y,y=z, kind='resid').set_axis_labels(xlabel='x-axis', ylabel='z-axis')
#as a hex plot
sns.jointplot(x=y,y=z, kind='hex').set_axis_labels(xlabel='x-axis', ylabel='z-axis')
#as a density plot   
sns.jointplot(x=y,y=z, kind='kde', color='purple').set_axis_labels(xlabel='x-axis', ylabel='z-axis')
#do a desnity plot with scatter
sns.jointplot(x=y,y=z, kind='scatter', color='purple').plot_joint(sns.kdeplot,zorder=1, n_levels=30).set_axis_labels(xlabel='x-axis', ylabel='z-axis')
#or 
sns.jointplot(x=y,y=z, kind='kde', color='purple').plot_joint(sns.lineplot).set_axis_labels(xlabel='x-axis', ylabel='z-axis')

### create a boxplot

sns.boxplot(x=x, y=z)