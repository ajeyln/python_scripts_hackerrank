# Task
''' You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.'''

# Input Format
'''The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of N integers.'''

N = int(input())
integers = input().split()

if all(int(i) >= 0 for i in integers):
    if any(num == num[-1:] for num in integers):
        print("True")
    else:
            print("False")
else:
    print("False")