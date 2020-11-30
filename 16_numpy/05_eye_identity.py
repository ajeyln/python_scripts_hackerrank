#Task
'''
Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.'''

#Input Format
'''
A single line containing the space separated values of 0 and 1.
N denotes the rows.
M denotes the columns.'''

import numpy
numpy.set_printoptions(sign=' ')
n,m = map(int, input().split())
print(numpy.eye(n,m))