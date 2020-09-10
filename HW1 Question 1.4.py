# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:33:58 2020

@author: Menno Hoogenes
"""
import numpy as np
import scipy
import matplotlib.pyplot as plt
from astropy.table import QTable, Table, Column

#Computing the Condition number of matrix A for the three different values of e

e = np.array([1, 0.1, 0.01])
f1 = np.array([1, 2, 3])
f2 = np.array([1, 2, 3.05])
c0 = np.array([])
sf0 = np.array([])

for i in e:
    A = np.array([[1,2,3], [4,5,6],[8,10,12+i]])
    print('Matrix A for e =', i,':', '\n', A)
    print()
    c = np.linalg.cond(A, p=None)
    c0 = np.append(c0, c)
    print('Condition number c for matrix A (e =', i, '):', '\n', c)
    print()
    #Computing the scaled norm 
    u1 = np.linalg.solve(A, f1)
    u2 = np.linalg.solve(A, f2)
    sf = np.divide(np.linalg.norm(u1-u2), np.linalg.norm(f1))
    sf0 = np.append(sf0, sf)
    print('The scaled difference in norm of u1 and u2 for e =', i, ':', '\n', sf)
    print()

print()
print('The complete table with corresponding condition number of the matrix A and the scaled norm for all values of e:')
t = Table([e, c0, sf0], names=('e', 'Condition number', 'scaled norm'))
print()
print(t)
print()