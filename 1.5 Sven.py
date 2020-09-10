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

def gaussSeidel(A,f,method,TOL=1E-6,kmax=100):
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
            u = np.copy(u0)
        
        #If method input is forward do forward Gauss-Seidel method
        if method == 'forward':
            u[0] = (f[0]-A[0,1]*u[1]-A[0,2]*u[2])/A[0,0]
            u[1] = (f[1]-A[1,0]*u[0]-A[1,2]*u[2])/A[1,1]
            u[2] = (f[2]-A[2,0]*u[0]-A[2,1]*u[1])/A[2,2]
        
        if method == 'backward':
            u[2] = (f[2]-A[2,0]*u[0]-A[2,1]*u[1])/A[2,2]
            u[1] = (f[1]-A[1,0]*u[0]-A[1,2]*u[2])/A[1,1]
            u[0] = (f[0]-A[0,1]*u[1]-A[0,2]*u[2])/A[0,0]
        
        #calculate rrs
        r_k = f - np.dot(A,u)
        r_norm = np.linalg.norm(r_k)
        rrs = np.divide(r_norm, r0_norm)
        
        #increase k
        k += 1
        #endloop
    
    if k < kmax-1:
        print(30*"#")
        print("{} Gauss-Seidel method".format(method))
        print(30*"#")
        print("A convergence has been reached!\n\nFound vector u:\n{}\n".format(u))
        print("Checking if Au = f...\nA: \n{}\nu: \n {}\nAu =\n{}\n(These values are rounded to an integer)\n\n".format(A,u,np.around(np.dot(A,u),2)))
        plt.plot(k_list,rrs_list, label=method)
        plt.title("RRS vs k")
        plt.yscale("log")
        plt.xlabel("k")
        plt.ylabel('rrs')
        plt.legend(loc=1)
        plt.xlim(0,6.5)
        return u, k_list, rrs_list
    else:
        print("No convergence reached before selected maximum amount of iterations")

uf, k_listf, rrs_listf = gaussSeidel(A,f,'forward')
ub, k_listb, rrs_listb = gaussSeidel(A,f,'backward')

