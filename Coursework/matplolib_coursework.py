# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:12:00 2019

@author: zee-erika
"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,100,400)
y=np.cos(x)
z=2*x**2
#plt.plot(x,y)

######################## 
fig=plt.figure()
ax=fig.add_subplot(111)
# top two lines are equvivalent to #fig,ax=plt.subplots(111)

ax.plot(x,y,color='blue',linewidth=2)
ax.set(xlim=[0,100])
ax.set(ylim=[-1,1])
ax.set(xlabel='x-axis')
ax.set(ylabel='y-axis')
ax.set(title='example_1' )
plt.show()


#############

fig,ax=plt.subplots()
ax.fill_between(x,y,z,color='green')
ax.plot(x,z,color='black', linewidth=5)
plt.show()

############

df={'x':x,'t':y}

fig,ax=plt.subplots()
ax.plot('x','t',color='black', linewidth=1, data=df)
plt.show()

############
a1=[0,1,2,3,4,5,6,7,8,9]
a2=[5,10,20,30,40,50,60,70,80,90]
fig,ax=plt.subplots()
ax.bar(a1,a2, ls='--', lw=5,edgecolor='red')
plt.show()

plt.bar(x,y, width=3, ls='dashed', lw=5, ec='red')
plt.show()
""" ls= linestyle lw= linewidth ec= edge color"""

######## Stack plots
plt.stackplot(x,y,y*2,y*3)
plt.show()

###############

plt.plot(x,y, 'k8-.', lw=3, mec='r', ms=5, mfc='none',mew=2, label='a',visible=True)
plt.title('title', fontsize=50)
#plt.axes('equal')
plt.legend(loc='upper right')
plt.tick_params(axis='both', labelsize=18)
plt.tight_layout()
plt.show()

################
################ colormap
fig,ax=plt.subplots()
ax.scatter(x,y,c=y, cmap='winter_r')
plt.show()

c=np.array((a1,a2))
b=np.random.random((10,10))
plt.imshow(b, interpolation='none',cmap='copper')
plt.show()
plt.imshow(c)
#plt.imshow(a,interpolation='none',cmap='seismic')
plt.show()