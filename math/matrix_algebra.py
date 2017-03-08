# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3],
               [2, 7, 4]])
B = np.matrix([[1, -1],
               [0, 1]])
C = np.matrix([[5, -1],
               [9, 1],
               [6, 0]])
D = np.matrix([[3, -2, -1],
               [1, 2, 3]])
u = np.matrix([6, 2, -3, 5])
v = np.matrix([3, 5, -1, 4])
w = np.matrix([1, 8, 0, 5]).T
alpha = 6

# 1 Matrix Dimensions
A.shape # (2, 3)
B.shape # (2, 2)
C.shape # (3, 2)
D.shape # (2, 3)
u.shape # (1, 4)
w.shape # (4, 1)

# 2 Vector Operations
u + v # [9, 7, -4, 9]
u - v # [3, -3, -2, 1]
alpha * u # [36, 12, -18, 30]
float(np.dot(u, v.T)) # 51. To avoid transposing, specify u, v as np.arrays
np.linalg.norm(u) # 8.6023252670426267

# 3 Matrix Operations
A + C # Not defined 
A - C.T # [[-4, -7, -3],[3, 6, 4]]
C.T - 3 * D # [[-4, 15, 9], [-4, -5, -9]]
B * A # [[-1, -5, -1], [2, 7, 4]]. Can also do np.matmul(B, A) or np.dot(B, A)
B * A.T # Not defined        
B * C # Not defined 
C * B # [[5, -6], [9, -8], [6, -6]]
B ** 4 #[[1, -4], [0, 1]]
A * A.T # [[14, 28], [28, 69]]
D.T *D # [[10, -4, 0], [-4, 8, 8], [0, 8, 10]]

