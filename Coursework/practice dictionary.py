# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:39:48 2019

@author: zee-erika
"""

""" practice dict by writing out a simple substitution code where each letter is equal to a number"""

import string
import numpy as np
l_characters=list(string.ascii_lowercase)
l_numbers=list(np.arange(0,26,1))
#a=(zip(l_characters,l_numbers))
#dict(a) write a loop

for i,x in enumerate(l_characters):
    print(x)
    print(i)
    