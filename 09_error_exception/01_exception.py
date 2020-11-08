'''You are given two values a and b.
Perform integer division and print a/b.'''

#Input Format
'''
The first line contains T, the number of test cases.
The next T lines each contain the space separated values of a and b.'''

for i in range(int(input("Please Enter the number of test cases: "))):
    try:
        a,b=map(int,input("Enter two numbers(please keep space between two numbers): ").split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)