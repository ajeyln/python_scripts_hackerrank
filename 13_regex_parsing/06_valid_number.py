#Task 
'''You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.'''

#Input Format
'''The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.'''

import re

n = int(input())
pattern = re.compile(r'^[7-9]\d{9}$')
numbers = [input() for x in range(n)]

for number in numbers:
    if pattern.match(number):
        print('YES')
    else:
        print('NO')