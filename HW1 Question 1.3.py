# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:13:12 2020

@author: Menno Hoogenes
"""
import matplotlib.pyplot as plt
import numpy as np

#Making coefficient matrix A and right-hand side vector b
#after doing in = out for all reactors (c1, c2, c3, c4, c5)
A = np.array([[6, 0, -1, 0, 0], [-3,3,0,0,0], [0,-1,9,0,0], [0,-1,-8,11,-2], [-3,-1,0,0,4]])
print('Coefficient matrix A:', '\n', A)
print()

b = np.array([50,0,160,0,0])
print('Right-hand side vector b:', '\n', b)
print()

#Computing solution vector c
#And checking if A*c = b
c = np.linalg.solve(A,b)
r = b - np.dot(A,c)
print('The approximate solution vector c:', '\n', c)
print()
print('The residual vector r:', '\n', r, '\n', 'Hence, r = 0 by approximation')