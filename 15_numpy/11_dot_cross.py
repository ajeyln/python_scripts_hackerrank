# Task
'''
You are given two arrays A and B. Both have dimensions of NXN.
Your task is to compute their matrix product.'''

# Input Format
''' The first line contains the integer N.
The next N lines contains N space separated integers of array N.
The following N lines contains N space separated integers of array B.'''

import numpy

a=int(input())

arr1=numpy.array([list(map(int,input().split())) for x in range(a)])

arr2=numpy.array([list(map(int,input().split())) for y in range(a)])

print(numpy.dot(arr1,arr2))