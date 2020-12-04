# Task
''' You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
 Replace these consecutive occurrences of the character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.'''

# Input Format
'''A single line of input consisting of the string S.'''

from itertools import groupby

for i, n in groupby(input()):
        a = list(n)  
        print("(", len(a), ", ", a[0], ")", end = " ", sep = "")