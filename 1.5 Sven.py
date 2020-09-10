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

#define zero-initial guess
u0 = np.zeros(3)

#Find initial rrs
r0_norm = np.linalg.norm(f - np.dot(A,u0))
rrs = np.divide(r0_norm, r0_norm)

def u1(f1,u2,u3):
    global A
    return (f1-A[0,1]*u2-A[0,2]*u3)/A[0,0]

def u2(f2,u1,u3):
    global A
    return (f2-A[1,0]*u1-A[1,2]*u3)/A[1,1]

def u3(f3,u1,u2):
    global A
    return (f3-A[2,0]*u1-A[2,1]*u2)/A[2,2]

k = 0
TOL = 10**(-6)

while rrs > TOL and k < 100:
    if k == 0:
        u = np.copy(u0)
    tempu = np.zeros(3)
    tempu[0] = u1(f[0],u[1],u[2])
    tempu[1] = u2(f[1],u[0],u[2])
    tempu[2] = u3(f[2],u[0],u[1])   
    u = np.copy(tempu)
    
    r_k = f - np.dot(A,u)
    r_norm = np.linalg.norm(r_k)
    rrs = np.divide(r_norm, r0_norm)
    k += 1

if k < 99:
    print('A convergence has reached. Found vector u:\n',u)