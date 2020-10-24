# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
# The first line contains n. The second line contains an array  a[]  of n integers each separated by a space.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    a=list(sorted(set(arr)))
    print(a[-2])
