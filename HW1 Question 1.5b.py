# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:13:20 2020

@author: Menno Hoogenes
"""

import numpy as np
import scipy
import matplotlib.pyplot as plt

#Defining matrix A and right-hand side vector f
A = np.array([[ 6,-1,-1],
              [ 6, 9, 1],
              [-3, 1,12]])

f = np.array([3,40,50])

#Define initial guess and boundary conditions
u0 = np.zeros(3)
k = 1
TOL = 10**(-6)
#Define function for Gauss Seidel method
#with matrix A, right hand side vector f and initial guess u0
def GaussSeidelf(A, f, u0, TOL, k):
    #Initial relative residual norm
    r0n = np.linalg.norm(f - np.dot(A,u0))
    rrs = np.divide(r0n, r0n)
    #Create empty list for the scaled residual norm values and iteration numbers
    srn = [rrs]
    kl = [0]
    u = np.copy(u0)
    #Using a while loop for the iterations
    while rrs > TOL and k < 50:
        #Creating a temporary vector and creating the next guess
        u[0] = (f[0] - A[0,1]*u[1] - A[0,2]*u[2])/A[0,0]
        u[1] = (f[1] - A[1,0]*u[0] - A[1,2]*u[2])/A[1,1]
        u[2] = (f[2] - A[2,0]*u[0] - A[2,1]*u[1])/A[2,2]
        #Copying it into u0, which will be the new guess input
        # Computing next iteration number k and checking if the boundary conditions fulfil
        rk = f - np.dot(A,u)
        rn = np.linalg.norm(rk)
        rrs = np.divide(rn, r0n)
        srn.append(rrs)
        kl.append(k)
        k += 1 
    return u, kl, srn

def GaussSeidelb(A, f, u0, TOL, k):
    #Initial relative residual norm
    r0n = np.linalg.norm(f - np.dot(A,u0))
    rrs = np.divide(r0n, r0n)
    #Create empty list for the scaled residual norm values and iteration numbers
    srn = [rrs]
    kl = [0]
    u = np.copy(u0)
    #Using a while loop for the iterations
    while rrs > TOL and k < 50:
        #Creating a temporary vector and creating the next guess
        u[2] = (f[2] - A[2,0]*u[0] - A[2,1]*u[1])/A[2,2]
        u[1] = (f[1] - A[1,0]*u[0] - A[1,2]*u[2])/A[1,1]
        u[0] = (f[0] - A[0,1]*u[1] - A[0,2]*u[2])/A[0,0]
        #Copying it into u0, which will be the new guess input
        # Computing next iteration number k and checking if the boundary conditions fulfil
        rk = f - np.dot(A,u)
        rn = np.linalg.norm(rk)
        rrs = np.divide(rn, r0n)
        srn.append(rrs)
        kl.append(k)
        k += 1 
    return u, kl, srn

u, kl, srn = GaussSeidelf(A, f, u0, TOL, k)
u1, kl1, srn1 = GaussSeidelb(A, f, u0, TOL, k)

#Plotting
plt.plot(kl,srn, label='forward')
plt.plot(kl1, srn1, label='backward')
plt.legend()
plt.yscale("log")
plt.xlabel("k")
plt.ylabel('rrs')


