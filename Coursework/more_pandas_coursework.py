# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:20:17 2019

@author: zee-erika
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
df1=pd.read_csv('pandas_concat_1.csv')
df2=pd.read_csv('pandas_concat_2.csv')

df3=pd.concat([df1,df2])
df3=df3.reset_index()

### add a new row

df4=pd.DataFrame([['Pinto',25,80]],columns=['Car','Fuel Milage','Horsepower'])
df5=pd.concat([df3,df4]) 
df5=df5.reset_index()

### add a new column

df5['HP:FM']=df5['Horsepower']/df5['Fuel Milage']
print(df5.head())


############ show column labels ########### 
df.columns.values

### sort columns

df5.sort_values('HP:FM', ascending=False)

######################

#print(df5['Car'].value_counts())
a=df5['Car'].value_counts()

plt.hist(df5['Car'],8)
###################
X=df5['Horsepower']
Y=df5['Fuel Milage']
plt.subplot(121)
plt.plot(X,Y, 'r*', label='FM')
plt.subplot(122)
plt.plot(X,df5['HP:FM'],'g*', label='ratio')
plt.show()

##########
plt.subplot(121)
sns.regplot(X,Y)
plt.subplot(122)
sns.regplot(X,df5['HP:FM'])
plt.subplot(221)
sns.residplot(X,Y)
plt.subplot(222)
sns.residplot(X,df5['HP:FM'])
plt.subplot(321)
sns.distplot(Y, hist=False)
plt.subplot(322)
sns.distplot(df5['HP:FM'], hist=False)
plt.show()
##########
from scipy import stats

df_anova=stats.f_oneway(X,Y)
print(df_anova)
pearson_coeff, p_val=stats.pearsonr(X,Y)
print('Pearson coeff = ', pearson_coeff,'p_val = ',p_val)

##########
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
X=X.values.reshape(-1,1)
Y=Y.values.reshape(-1,1)
YY=df5['HP:FM'].values.reshape(-1,1)
lm.fit(X,Y)
Y_pred=lm.predict(X)
plt.plot(X,Y_pred, label='fit')
plt.plot(X, Y, 'rx', label='data')
plt.show()
print("slope = ",lm.coef_, "intercept",lm.intercept_)
print('r^2 = ',lm.score(X,Y))
print("/n")
lm.fit(X,YY)
YY_predic=lm.predict(X)
plt.plot(X,YY_predic)
plt.plot(X,YY,'g<',label='data')
print("slope = ",lm.coef_, "intercept",lm.intercept_)
print('r^2 = ',lm.score(X,YY))
"""
######################################################

x=np.linspace(0,100,200)
y=2*(x)
z=np.cos(x)
yerr=0.5*y
xerr=0.1
plt.subplot(1,2,1)
plt.plot(x,y,'b',markersize=5,linewidth=2)
plt.title('sine')
plt.subplot(1,2,2)
plt.plot(x,z,'k',markersize=5,linewidth=2,label='cos' )
plt.show()
size=np.random.rand(200)*30
plt.scatter(x,y,size)
plt.errorbar(x,y,yerr)
plt.legend()
