# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:18:28 2020

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


#define matrix A
A = np.array([[ 6,-1,-1],
              [ 6, 9, 1],
              [-3, 1,12]])

#define right-hand side vector
f = np.array([3,40,50])

def gaussSeidel(A,f,TOL=10**(-6),kmax=100):
    #calculate initial r and rrs
    u0 = np.zeros(3)
    r0_norm = np.linalg.norm(f - np.dot(A,u0))
    rrs = np.divide(r0_norm, r0_norm)
    
    #initial k
    k = 0
    
    #lists for plotting residual norm and iterations
    k_list = []
    rrs_list = []
    
    #Gauss Seidel iterations:
    while rrs > TOL and k < kmax:
        #append k to k list and rrs to rrs list
        k_list.append(k)
        rrs_list.append(rrs)
        
        #if initial iterations set u values equal to 0
        if k == 0:
            u = np.zeros(3)
        
        #new temporary vector
        tempu = np.zeros(3)
        
        #Change each component according to Gauss Seidel method
        tempu[0] = (f[0]-A[0,1]*u[1]-A[0,2]*u[2])/A[0,0]
        tempu[1] = (f[1]-A[1,0]*u[0]-A[1,2]*u[2])/A[1,1]
        tempu[2] = (f[2]-A[2,0]*u[0]-A[2,1]*u[1])/A[2,2]
        
        #copy all values into vector u
        u = np.copy(tempu)
        
        #calculate rrs
        r_k = f - np.dot(A,u)
        r_norm = np.linalg.norm(r_k)
        rrs = np.divide(r_norm, r0_norm)
        
        #increase k
        k += 1
        #endloop
    
    if k < kmax-1:
        print("A convergence has been reached!\n Vector u:\n{}\n".format(u))
        print("Checking if Au = f...\nA: \n{}\n u: \n {}\n (Rounded:)Au =\n{}".format(A,u,np.around(np.dot(A,u),2)))
        return u, k_list, rrs_list
    else:
        print("No convergence reached before selected maximum amount of iterations")

u, k_list, rrs_list = gaussSeidel(A,f)

plt.plot(k_list,rrs_list)
plt.yscale("log")
plt.xlabel("k")
plt.ylabel('rrs')
