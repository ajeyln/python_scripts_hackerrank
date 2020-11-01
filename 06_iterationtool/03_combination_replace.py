'''You are given a string s.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.'''

from itertools import combinations_with_replacement

s, k = input().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))