'''The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.'''


s1 = int(input())
sl1 = set(map(int,input().split()))
s2 = int(input())
sl2 = set(map(int,input().split()))
print (len(sl1.intersection(sl2)))