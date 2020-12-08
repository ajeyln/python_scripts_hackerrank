#Task
'''You are given a 1-D array, A. Your task is to print the floor, ceil and rent of all the elements of A.'''

# Input Format
'''A single line of input containing the space separated elements of array A.'''

import numpy

numpy.set_printoptions(sign=' ')

a = numpy.array(input().split(),float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))