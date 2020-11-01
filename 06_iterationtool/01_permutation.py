'''You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.'''

from itertools import permutations

s, k = input().split(" ")
permutations = list(permutations(s, int(k)))
permutations.sort()

for i in permutations:
    print("".join(i))