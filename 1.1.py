# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:27:58 2020

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

#Define matrix A1
A1 = np.array([[7.,2.,1.],[1.,7.,1.],[3.,2.,7.]])
#LU factorization
P1,L1,U1 = scipy.linalg.lu(A1)

#plotting non-zero structure of L and U
pltL1 = plt.subplot(121)
pltL1.spy(scipy.sparse.csr_matrix(L1))
pltL1.set_title("L1",pad=20)
pltL1.set_xlabel('Column')
pltL1.set_ylabel('Row')

pltU1 = plt.subplot(122)
pltU1.spy(scipy.sparse.csr_matrix(U1))
pltU1.set_title("U1",pad=20)
pltU1.set_xlabel('Column')
#pltU1.set_ylabel('Row')

#check if L1U1 = A1
LU1 = np.dot(L1,U1)
print('Product of L1U1: \n',LU1,2*'\n','Matrix A1: \n', A1)

##################################################
print('\n',20*'#','\n')
##################################################
#Define matrix A2
A2 = np.array([[2,2,1],[1,1,1],[3,2,1]])
#LU factorization
P2,L2,U2 = scipy.linalg.lu(A2)

#check if L2U2 = A2 
LU2 = np.dot(L2,U2)
print('Product of L2U2: \n',LU2,2*'\n','Matrix A2: \n',A2)
PLU2 = np.dot(P2,LU2)
print('\nProduct of PLU: \n',PLU2,2*'\n','Matrix A2: \n',A2)