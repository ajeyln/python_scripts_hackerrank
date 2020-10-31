''' You are given a positive integer N.
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:
1
121
12321
1234321
123454321 '''

N = int(input())

for x in range(N + 1):
    print(((10**x - 1)//9)**2)