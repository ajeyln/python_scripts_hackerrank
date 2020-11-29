# Task
''' You are given a space separated list of nine integers. Your task is to convert this list into a 3 X 3 NumPy array.'''
# Input Format
''' A single line of input containing 9 space separated integers. '''

import numpy
print(numpy.array(input().split(), int).reshape(3,3))