# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:27:14 2019

@author: zee-erika
"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pandas_practice.csv', header=0)
df.head()  #prints the first 5 lines of the dataset
df.tail()
print(df.describe()) # basic stats for each column
df.info()
df.dropna() #drops the missing value
df.rename(columns={"B":"Bo"}, inplace=True)

plt.scatter(df['A'],df['C'])
plt.plot(df['A'][::2], df['C'][::2], 'r^')
df1=df['A']
df2=df['C']
plt.plot(df1[0:50],df2[0:50], 'g^')

df['A']=df['A']+1e17
plt.plot(df['A'], df['C'], 'go')
plt.show('Figure 1')

#methods for normalizing data
#simple scaling

df3=df['A']/df['A'].max()
df4=df['Bo']/df['Bo'].max()
df5=df['C']/df['C'].max()
plt.scatter(df3,df4)
plt.scatter(df3,df5)
plt.title('Feature Scaling')
plt.show('Figure 2')

# min-max method

df6= (df['A']-df['A'].min())/(df['A'].max()-df['A'].min())
df7= (df['Bo']-df['Bo'].min())/(df['Bo'].max()-df['Bo'].min())
df8= (df['C']-df['C'].min())/(df['C'].max()-df['C'].min())
plt.scatter(df6,df7)
plt.scatter(df6,df8)
plt.title('Min-Max Scaling')

plt.show('Figure 3')

#z-score method

df9= (df['A']-df['A'].mean())/(df['A'].std())
df10= (df['Bo']-df['Bo'].mean())/(df['Bo'].std())
df11= (df['C']-df['C'].mean())/(df['C'].std())
plt.scatter(df9,df10)
plt.scatter(df9,df11)
plt.title('Z-score Scaling')
plt.show('Figure 4')
"""
#Binning your data

df=pd.read_csv('pandas_practice2.csv', header=0, dtype='int64')
#define the binwidth
n=3 #number of bins
binwidth=(df['A'].max()-df['A'].min())/(n+1)
bins=range(min(df['A']),max(df['A']),int(binwidth))
bin_label = ['uno', 'dos', 'tres']
df['A_binned']= pd.cut(df['A'], bins, bin_label)
#plt.hist(df['A'],int(binwidth), index=bin_label)
"""