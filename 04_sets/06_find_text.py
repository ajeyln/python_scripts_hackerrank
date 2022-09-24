'''
Here, b occurs 3 times. It is printed first.
Both a and c occur 2  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string S has at least 3 distinct character 

from re import I

'''

from collections import Counter

[print(x,y) for x, y in Counter(sorted(input())).most_common(3)]




