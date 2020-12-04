# Task
'''You are given a two lists A and B. Your task is to compute their cartesian product AXB.'''

#Input Format
''' The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.'''

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))