# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 18:05:53 2019

@author: zee-erika
"""
""" practice dummy variables to convert string id's into numeric keys"""
import numpy as np
import pandas as pd

df=pd.read_csv('pandas_practice_dummy.csv')
df1=pd.get_dummies(df['Fuel'])
df1.to_csv('dummy.csv')