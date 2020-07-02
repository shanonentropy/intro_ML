# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 15:11:59 2019

@author: zee-erika
"""
'''Numpy/scipy rundown'''
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,50) #creates an array of 50 points between 0 and 2pi
y=np.sin(x)
y2=np.cos(x)
plt.plot(x,y, 'g<', markersize=3,label='sin')
plt.plot(x,y2, 'bo', markersize=5,label='cos') #other params include linestyle and linewidth
#hold(False) #clears out previous plot and puts the new one in
plt.legend()
#plt.legend(['sin','cos']) #alternative way
plt.show()
a=np.random.rand(200) #creates an array of 200 random numbers
b=np.sin(a)
size=np.random.rand(200)*20 #specify's the size of each point 
plt.scatter(a,b,size)
plt.show()

#### sub-plotting ####
'''subplt(x=nrow,y=ncolums,z=plot#) x and y specify how to put the subplots together e.g.
(1,2,xx) says subplots go in 1 row and 2 columns. the last entry specifies the order 
for each subplot with lowest number going to left'''
plt.subplot(1,2,1)
plt.plot(x,y)
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.show()

###### put error bars on graph

xerr= 0.05*x
yerr=0.1*y
y2_err=0.2*y2
#plt.errorbar(x,y,y_err,x_err)
plt.errorbar(x,y,yerr, xerr)
plt.show()

########### slicing and indexing

a=np.arange(0,100,5)
a[0:3] #first to third entry
a[:]  #all entries
a[::4] #every fourth

print(np.where(a/5>1))
print(np.min(a))
print(np.max(a))
print(np.std(a))
print(np.argmin(a))
print(np.argmax(a)) #highest value's index

b=np.linspace(0,10,10)
b=b.reshape(2,5)
b.sum(axis=0) #sums down the column
b.sum(axis=1) #sums across the row
c=np.eye(4) #creates a 4 * 4 identity matrix

########### example of image display 

from scipy.misc import face
img=face()
#plt.gray()
plt.imshow(img)

############## array creation and manipulation ######3

#create an empty array
a=np.zeros((5,5))  ### matrix of zeros
a.fill(5) # matrix re-populated with passed value
b=np.ones((5,5)) # unit matrix
c=np.identity(5) # creates a n*n identity matrix
d=np.array([[0,0,1,0,2],[0,0,1,0,2]]) # a matrix constructed by hand
e=d.T #transpose of d
d.size #returns the number of entries
d.shape #returns the shape (r * c) of the matrix
d.ndim #freturns the dimentions of the matrix
d[1:1] #pulls out value at index 1,1 (r, c)

### filtering 

f=np.arange(0,25,1)
f.reshape(5,5)
#to filter use boleen commands in the following arrangement
f[f>17]
f[f%7]
f[f<4]

[f<4] # the boleean matrix gives a true/false matrix, which when multipled by 
#the matrix returns an array with our values

##### Bolean logic can be combined with np.where() to find array index of 
##### particular values e.g
f[np.where(f==0)]