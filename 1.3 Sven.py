# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:31:36 2020

@author: Sven
"""


import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sym 
from scipy import optimize
from numpy import linalg as LA
from mpl_toolkits import mplot3d

#Balance for each reactor:
#Reactor 1: 5*10 + C3 = 3*C1 + 3C1
#           -6C1 + C3  = 50
#Reactor 2: 3C1 = C2 + C2 + C2 
#           3C1 - 3C2 = 0
#Reactor 3: 8*20 + C2 - C3 - 8C3 = 0
#           + C2 - 9C3 = 160
#Reactor 4: C2 + 8C3 + 2C5 = 11C4
#           C2 + 8C3 + 2C5 - 11C4 = 0
#Reactor 5: 3C1 + C2 - 2C5 - 2C5
#           3C1 + C2 - 4C5 = 0

#Form a coefficient matrix A so that Ac = m --> c is a vector containing concentrations of reactor 1 to 5. Vector m is the right hand side vector
A = np.array([[ 6, 0,-1, 0, 0],
              [-3, 3, 0, 0, 0],
              [ 0,-1, 9, 0, 0],
              [ 0,-1,-8,11,-2],
              [-3,-1, 0, 0, 4]])

m = np.array([50,0,160,0,0])

print("Coefficient matrix A: \n",A,'\n\n right-hand side vector m: \n',m,'\n\n')


#Compute the solution vector c using np.linalg.solve
c = np.linalg.solve(A,m)
print('The solution for c in Ac = m is: \n',c)

#rounding to 2 decimals
print("\n\nRounded to 2 decimals each value of C is:")
for i in range(len(c)):
    print("C"+str(i)+': ' + str(round(c[i],2)))
print('\n\n')


#Check if this is indeed correct by multiplying A and c to check if this equals to m
check = np.dot(A,c)
print('Check by multiplying A * c. The result is: \n',check,'\n\n Rounded to one decimal:')
#round the check so it is easier to compare
for i in range(len(check)):
    print('m['+str(i)+'] = ' +str(round(check[i],0)))

print('\n\nSo the found vector c is correct!')


