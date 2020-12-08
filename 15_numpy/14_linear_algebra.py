#Task
'''
You are given a square matrix A with dimensions NXN. Your task is to find the determinant(Round the answer to 2 places after the decimal.)'''

#Input Format
'''The first line contains the integer N.
The next N lines contains the N space separated elements of array A.'''

import numpy
n=int(input())
a=numpy.array([input().split() for _ in range(n)],float)
numpy.set_printoptions(legacy='1.13') #important
print(numpy.linalg.det(a))