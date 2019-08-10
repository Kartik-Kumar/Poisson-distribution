# -*- coding: utf-8 -*-
"""
Created on Thu May  2 02:10:51 2019


"""
"""
problem:Affect of changing value of mu.
    
    
    
"""
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

bar_width=.30
n_group=8
mu1=0.33
mu2=0.59
mu3=1.29
p1=[]
p2=[]
p3=[]
for i in range(0,8):
    p1.append(round(poisson.pmf(i, mu1),6))
    p2.append(round(poisson.pmf(i, mu2),6))
    p3.append(round(poisson.pmf(i, mu3),6))
print("-------------------------------------------------------------------")
print("value of K\tp1\t\tp2\t\tp3")
print("-------------------------------------------------------------------")

for i in range(0,6):
    print(i,"\t\t",p1[i],"\t",p2[i],"\t",p3[i])
    

fig,ax=plt.subplots()
index=np.arange(n_group)
rects1=plt.bar(index,p1,bar_width,color='b',label="p1")
rects1=plt.bar(index+bar_width,p2,bar_width,color='g',label="p2")
rects1=plt.bar(index+2*bar_width,p3,bar_width,color='y',label="p3")
plt.xticks(index + bar_width, list(range(0,8)))
plt.ylabel('probability')
plt.title('probability bargraph')
plt.xlabel('K')