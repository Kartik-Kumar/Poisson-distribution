# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:58:13 2019

@author: kartik kumar

file structure project
"""
#conside the problem- 
#Given N availble address and r record to be stored what is the probability of an address getting 0,1,2,3... records assigned to it ?
#if an address is assigned more than one record , then a collision occours .
#poissoon distribution is used to calculate the number of overflowing record where MU = R/N , 
          # where R=no. of records stored and N is available address
# considering 1000 recods to be stored in 1000 location
          
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np
r=1000
n=1000
mu=r/n
prob=[]
k=list(range(0,7))

for i in k:
    prob.append(round(poisson.pmf(i, mu),4))

y_pos = np.arange(len(prob))
plt.bar(y_pos, prob, align='center',color=['black', 'red', 'green', 'blue', 'cyan'],edgecolor='blue')
#plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.title('probability of collision')
plt.xlabel('K')

for i in range(len(prob)):
    print('the probability of an address getting',i,'records assigned-->',prob[i],"\n")
print("-------------------********---------------------******--------------------------")
for i in range(len(prob)):
    print('the number of address which have',i,'records-->',int(round(prob[i]*1000,0)),"\n")

sum=0
for j in list(range(2,7)):
    sum=sum+int(round(prob[j]*1000,0))*(j-1)
print("******************************************")
print('*  Total number if over flowing is ',sum," *")
print("******************************************")
