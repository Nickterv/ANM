# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 11:00:30 2020

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


#define function F(u)
def F(u):
    return u**2 - 2

def findRoot(func,guess,tol,rtol):
    return scipy.optimize.newton(F,1,tol=1e-40,rtol=rtol)

u0_1 = 1
tol = 1e-40
rtol1 = 1e-6
rtol2 = 1e-8
rtol3 = 1e-10

rtol = [rtol1, rtol2, rtol3]

u = np.zeros((len(rtol),2))
for i in range(len(rtol)):
    u[i,0] = findRoot(F,u0_1,tol,rtol[i])
    u[i,1] = np.abs(u[i,0]-np.sqrt(2))

print("\n\nTable 1 - Computation of sqrt(2) using scipy.optimize.newton() \nwith initial guess of u = 1\n")
df = pd.DataFrame({"rtol":rtol, "Found root":u[:,0], "absolute difference":u[:,1]})
print(df)
print(2*'\n')
#############################
u0_2 = -1
rtol_2 = 1e-6
print("")