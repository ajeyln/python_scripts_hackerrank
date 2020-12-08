# Task
''' You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column).
 Your task is to concatenate the arrays along axis 0.'''

# Input Format
''' The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.'''

import numpy

n, m, p = map(int, input().split())    #assign n,m,p

src1 = " ".join(input() for _ in range(n))  #matrix1
ind1 = numpy.array(src1.split(), int)
ind1.shape = (n, p)

src2 = " ".join(input() for _ in range(m)) #matrix2
ind2 = numpy.array(src2.split(), int)    
ind2.shape = (m, p)

print(numpy.concatenate((matrix1, matrix2), axis=0))