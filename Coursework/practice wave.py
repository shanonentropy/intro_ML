# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 16:24:47 2019

@author: zee-erika
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

A=2 #amplitude
fq=(np.pi)*2*(np.radians(10)) #frequency of the signal
fq2=np.pi*2*np.radians(45)
timestep=0.1
x=np.arange(00,500,timestep)

#eauation for the signal
y=(A**2)*np.cos(fq*x)
yy=((A)**2)*np.sin(fq2*x)
yz=0.5*(y+yy)
plt.plot(x,yz)
plt.show()

#take the FFT of the signal

sig_fft=fftpack.fft(yz)
#signal power
power=np.abs(sig_fft)
#signal frequency
freq=fftpack.fftfreq(yz.size, d=timestep)
plt.plot(freq,power)
plt.xlim(0,)
