'''You are given a string s.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.'''

from itertools import combinations

s , n  = input().split()

for i in range(1, int(n)+1):
    for j in combinations(sorted(s), i):
        print(''.join(j))