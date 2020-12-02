# Task
'''You are given a string s.
Your task is to find the indices of the start and end of string k in s.'''

#Input Format
''' The first line contains the string s.
The second line contains the string k.'''

import re
S = input()
k = input()
pattern = re.compile(k)
r = pattern.search(S)
if not r: print("(-1, -1)")
while r:
    print("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)