# Task
''' You are given a 2-D array of size X.
Your task is to find:

The mean along axis 1
The var along axis 0
The std along axis None'''

# Input Format
''' The first line contains the space separated values of N and M.
The next N lines contains M space separated integers.'''

import numpy
n,m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = numpy.array(b)

numpy.set_printoptions(legacy='1.13')
print(numpy.mean(b, axis = 1))
print(numpy.var(b, axis = 0))
print(numpy.std(b))
