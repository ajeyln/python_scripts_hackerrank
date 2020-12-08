#Task
''' You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:
Add (A + B)
Subtract (A - B)
Multiply (A * B)
Integer Division (A / B)
Mod (A % B)
Power (A ** B)'''

# Input Format
'''The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B. '''

import numpy
N, M = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
B = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
print(numpy.add(A,B), numpy.subtract(A,B), numpy.multiply(A,B,), numpy.floor_divide(A,B), numpy.mod(A,B), numpy.power(A,B), sep = "\n")