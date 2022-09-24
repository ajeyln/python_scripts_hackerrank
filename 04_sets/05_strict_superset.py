'''
SetA = 1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
No. of Subsets = 2
Subset1 = 1 2 3 4 5
Subset2 = 100 11 12
Set A is the strict superset of the set([1,2,3,4]) but not of the set([100,11,12]) because 100 is not in set A .
Hence, the output is False.'''

seta = set(map(int, input().split()))

l=True
for i in range(int(input())):
    setb = set(map(int, input().split()))
    l = (l and setb.issubset(seta) and len(seta)>len(setb))
print(l)
