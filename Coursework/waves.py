# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:29:05 2019

@author: zee-erika
"""
''' create a cosine wave of different train size'''
import numpy as np
import matplotlib.pyplot as plt

#wavelength of light
#t2=np.arange(10,20,0.1)
l=2
c=300 #speed of light

Fs=((2*np.pi*c)/l)*100 #sampling rate
stepsize=(1/Fs)
#k=2*np.pi*(1/l)
#freq= 2*np.pi*(np.radians(45))
freq=(c/l)
t=np.arange(0,2,stepsize)
Eo= 1
# wavetrain equation    
EC=(Eo**2)*np.cos(2*np.pi*freq*t)
ES=Eo**2*np.sin(freq*t)
EE=0.5*(EC+np.imag(ES))
plt.plot(t,ES)
plt.plot(t,EC)
#plt.plot(t,EE)

from scipy import fftpack
wfft=fftpack.fft(EC)
power=np.abs(wfft)
sample_freq = fftpack.fftfreq(EC.size, d=stepsize)
plt.show('Figure 2')
plt.plot(sample_freq,power,'--')

w2fft=fftpack.fft(ES)
power2=np.abs(w2fft)
sample_freq2 = fftpack.fftfreq(ES.size, d=stepsize)
plt.plot(sample_freq2,power2,'x')
"""
w3fft=fftpack.fft(ES)
power3=np.abs(w3fft)
sample_freq3 = fftpack.fftfreq(ES.size, d=stepsize)
plt.plot(sample_freq3,power3,'+')   """
plt.xlim(-0.0,110)
#plt.ylim(0.0,50)
 

