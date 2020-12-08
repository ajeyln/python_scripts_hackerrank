#Task
'''You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.'''

# Input Format
'''A single line containing the space-separated integers.'''

import numpy
x = tuple(map(int,(input().split())))

arr1 = numpy.zeros((x), dtype = numpy.int)
print(arr1)
    
arr2 = numpy.ones((x), dtype = numpy.int)
print(arr2)