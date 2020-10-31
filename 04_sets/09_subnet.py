'''You are given two sets, A and0 B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.'''


n = int(input())

for i in range(n):
    a = int(input())
    set_a = set(input().split())
    b = int(input())
    set_b = set(input().split())
    out_set = set_a.difference(set_b)
    if len(out_set) == 0:
        print(True)
    else:
        print(False)