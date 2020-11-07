'''Perform append, pop, popleft and appendleft methods on an empty deque d.'''

# Input Format
'''The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.'''

from collections import deque

d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)
[print(x, end=' ') for x in d]