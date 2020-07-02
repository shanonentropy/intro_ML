# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:13:27 2019

@author: zee-erika
"""

########### practice Pandas ###########

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('multivar_reg.csv')

#basic commands to get info on the dataset

df.head()
df.tail()
df.describe()
df.info()

#### Basic commands to get stats from the dataset if not using describe func

df['t'].mean()
df['t'].std()
df['t'].min()
df['t'].max()
df['t'].count()

#### sorting function #####
aa=df.sort_values('t', ascending=False)

##### slicing dataframe to create subframes to plot ####
a=df['t']
b=df['ft']
plt.plot(a,b, 'x')
plt.show('Figure 1')
# an alternative writing style is 

plt.scatter(df.s,df.fts)
plt.show() 
#slice the first 20 rows
print(df[10:20]) # slice the entire dataframe
print(df.fts[20:30]) #slice on the specified column
print(df.ft[::2]) # skip two rows everytime
#slice multiple columns
print(df[['t','s']]) # you are passing a [list] to df header [] hence the double brackets
df[['t','s']].head()
df[['t','s']][::10] #for the chosen columns slices out every tenth row

##### fancier slicing ######
# use loc to specify the rows and columns to slice 
# loc[row:row, [['column header', 'column header']]]

df.loc[:,['t','s']] #all rows of t and s column
df.loc[2,['t','s']]# row 2 for selected columns
df.loc[:10,['t','s']]# row 0-10 for selected columns
df.loc[2:10,['t','s']] # rows 2-10 for selected columns
##### use iloc when using index number for column identifier
df.iloc[2:10,[0,1]]

################ Filtering Data ##################
# when filtering by value
df[df['t']>0] # for this dataframe's column labeled t, show all vals > 0
# when filtering to show only certain values
#### for the column labeled t, isin method looks for items in the list
df[df['t'].isin([-40,0,5,100])]

################ Assinging Values ################
df.iloc[0,[0]]=-39.5
### or 
df.loc[1,['t']]=-35.1
df.head()
#### you can also multiply or divide an any row or column to change it's value

############# Creating a new column ################
# take a difference of ft and fts columns
df['ft-fts']=df.ft-df.fts
df.head()

############# Remanming columns ###################

df.rename(columns={'ft-fts':'difference'},inplace=True)
# this command reads as: with dataframe df, apply method rename, passing it
# the following values, columns which are equal to dictionary of 'exisiting name'
# is equal to 'new name'. inplace = True means save this outcome 
# if not using inplace keyword then write 
## df=df.rename(columns={'something':'another thing'})
############ you can use the above command to change one of more column names
df.head()

# When chainging names of all columns simply set it equal to a list
df.columns=['temp', 'strain', 'temp_resp','strain_resp']
df.head() 
