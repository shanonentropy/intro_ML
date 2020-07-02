# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:20:04 2019

@author: zee-erika
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df=pd.read_csv('pandas_practice.csv')
#basic descriptors
df.describe() #skips NaN values

"""practice categorical variables"""
df1=pd.read_csv('pandas_practice_dummy.csv')
df1.rename(columns={'Car':'Cars'}, inplace=True)
number_of_cars=df1['Cars'].value_counts()
print(number_of_cars)
plt.boxplot(number_of_cars)
plt.show()

#groupby sorting

df_h=pd.read_csv('heatmap.csv')
df_grp=df_h.groupby(['Fuel Milage']).mean()
print(df_grp)

#ANOVA test

df_anova=df_h[['Fuel Milage','Horsepower']]  #create a pd with sets to be compared
anova_results=stats.f_oneway(df_anova['Fuel Milage'],df_anova['Horsepower'])
print(anova_results) #looking for large  F stat value and small P 

#correlation
sns.regplot('Fuel Milage', 'Horsepower',data=df_h, x_ci=95)

#Pearson Correlation

Pearson_coeff, p_value=stats.pearsonr(df_h['Fuel Milage'], df_h['Horsepower'])
print("Pearson coefficient and the p value are", Pearson_coeff, p_value)

"""for Pearson analysis the correlation is strong when coeff is close to +/-1
and p value is less than 0.001; moderate when p<0.005 and weak when P<0.1. There
is no relationship when coeff is 0 and no certainty when P>0.1"""

#