# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:59:40 2018

@author: zahmed
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing #data processing module

#a=np.tile([0,0,0,0,0.1,0.2,0.3,0.4,0.45,0.5,0.45,0.4,0.3,0.2,0.1,0,0,0,],3)
a=np.arange(0,100,1)
a1=np.append(a,[100, 100, 100,1000, 1000, 1000, 0,0,0])
aa=5*np.sin(2*a1+6)+15
plt.plot(aa)

a_array = np.tile(aa,[200,1])
#print(np.shape(a_array))
b_array = np.transpose(a_array, [1, 0])        
min_max_scaler = preprocessing.MinMaxScaler()
b_array_minmax = min_max_scaler.fit_transform(b_array)
plt.figure('fig 2')
plt.imshow(b_array_minmax)
