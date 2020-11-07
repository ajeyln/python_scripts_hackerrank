'''The first line contains integers, n and n separated by a space.
The next n lines contains the words belonging to group A.
The next m lines contains the words belonging to group B.'''

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input().split())

for i in range(1,n+1):
    d[input()].append(str(i))
    
for i in range(m):
    print (' '.join(d[input()]) or -1)