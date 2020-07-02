# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 12:31:53 2019

@author: zee-erika
"""

######### data analysis ############

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df=pd.read_csv('multivar_reg.csv')
df.columns=['temp', 'strain', 'temp_resp', 'temp_strain_resp']

print('temperature range =', df.iloc[:,0].max()-df.iloc[:,0].min())
print('strain range =', df['strain'].max()-df['strain'].min())

#### plot data ####
plt.scatter(df['temp'], df['temp_resp'])
plt.show()
plt.scatter(df['temp'], df['temp_strain_resp'])
plt.scatter(df['strain'],df['temp_strain_resp'])
plt.show()

###### simple correlation analysis ########
''' shows how well data is correlated to linear curve '''
#regplot
sns.regplot(df['temp'],df['temp_resp'])
plt.show()
#sns.regplot(df['strain'],df['temp_strain_resp'])

#### Pearson's test #####
Pearsons_coeff, pval=stats.pearsonr(df['temp'],df['temp_resp'])
print("Pearson coefficient = ", Pearsons_coeff, "p-value = ", pval)
''' shows high degree of correlation and certainty'''
Pearsons_coeff1, pval1=stats.pearsonr(df['temp_resp'],df['temp_strain_resp'])
print('\n')
print('Correlation between temp and mixed temp and strain response functions is')
print("Pearson coefficient = ", Pearsons_coeff1, "p-value = ", pval1)

##### ANOVA test ########
anova_results=stats.f_oneway(df['temp_resp'],df['temp_strain_resp'])
print(anova_results)

######### Normalize data so as to show distriubtion plots together
# Feature Scaling
a=df['temp']/df['temp'].max()
b=df['strain']/df['strain'].max()
c=df['temp_resp']/df['temp_resp'].max()
d=df['temp_strain_resp']/df['temp_strain_resp'].max()
sns.distplot(c, hist=False)
sns.distplot(d, hist=False)
plt.title('Feature scaling')
plt.show()
# Min-Max Scaling
a1=(df['temp']-df['temp'].min())/(df['temp'].max()-df['temp'].min())
b1=(df['strain']-df['strain'].min())/(df['strain'].max()-df['strain'].min())
c1=(df['temp_resp']-df['temp_resp'].min())/(df['temp_resp'].max()-df['temp_resp'].min())
d1=(df['temp_strain_resp']-df['temp_strain_resp'].min())/(df['temp_strain_resp'].max()-df['temp_strain_resp'].min())
sns.distplot(c1, hist=False)
sns.distplot(d1, hist=False)
plt.title('min-max scaling')
plt.show()
# Z-score Scaling
a2=(df['temp']-df['temp'].mean())/(df['temp'].std())
b2=(df['strain']-df['strain'].mean())/(df['strain'].std())
c2=(df['temp_resp']-df['temp_resp'].mean())/(df['temp_resp'].std())
d2=(df['temp_strain_resp']-df['temp_strain_resp'].mean())/(df['temp_strain_resp'].std())
sns.distplot(c2, hist=False)
sns.distplot(d2, hist=False)
plt.title('z-score scaling')
plt.show()

############ fit to normailzed data ##############
# evaluate data by fitting the data to linear func and look at residuals plot

sns.residplot(a2,c2)
plt.title('residual of temp response')
sns.residplot(a2,d2)
#plt.show()
# fit to linear func using scikitlearn and evaulate R^2
from sklearn.linear_model import LinearRegression
lm=LinearRegression() #calls the method linear regression
X=pd.DataFrame(a2)
Y=pd.DataFrame(c2)
lm.fit(X,Y) # (independent, dependent) frames are passed to methods fit in linreg
Y_predicted=lm.predict(X)
plt.plot(X,(Y-Y_predicted), 'g+')

print("slope = ", lm.coef_, "intercept = ",lm.intercept_)
print('R^2 = "=',lm.score(X,Y))
