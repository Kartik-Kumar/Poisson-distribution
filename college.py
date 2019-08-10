# -*- coding: utf-8 -*-
"""
Created on Thu May  2 01:03:32 2019

@author: 
"""

"""
PROBLEM STATEMENT:
    Student arrive at the rate of 72 per hour in the college.What is the probability of k student
    arriving in 4 min?
    a)5 students,  b)not more than 3 students, c) more than 3 students
"""

from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

rate_in_hour=72
time=4    # in minute
mu=(rate_in_hour/60)*time
print("mean=",mu)
print()


prob=[]
k=range(0,13)

for i in k:
    prob.append(round(poisson.pmf(i, mu),3))

y_pos = np.arange(len(prob))
plt.bar(y_pos, prob, align='center',color=['black', 'red', 'green', 'blue', 'cyan'],edgecolor='blue')
#plt.xticks(y_pos, objects)
plt.ylabel('probability')
plt.title('probability bargraph')
plt.xlabel('K')

for i in range(len(prob)):
    print('the probability of ',i,'students arrived in 4 min-->',prob[i],"\n")
    
#solution for A)5 students
k=5
print("the probability of 5 student arriving in 4 min --->",round(poisson.pmf(5, mu),3),'i.e.',round(poisson.pmf(5, mu),3)*100,'%')

#solution B) not more than 3 student
k=3
prob=round(poisson.cdf(k, mu),5)
print("the probability of not more than 3 student arriving in 4 min --->",prob)

#solution C)more than 3 students
print("the probability of more than 3 student arriving in 4 min --->",1-prob)