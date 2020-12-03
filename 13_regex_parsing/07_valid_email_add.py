'''The first line contains a single integer, n, denoting the number of email address.
Each line i of the n subsequent lines contains a name and an email address as two space-separated values'''

import re
n = int(input())
for p in range(n):
    x, y = input().split(' ')
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)