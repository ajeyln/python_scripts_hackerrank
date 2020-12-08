# to find hash value of a tuple
# Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. 

if __name__ == '__main__':
    n = int(input()) # number of elements to create list
    integer_list = input().split() # need to give "n" number integers and sepated with space
    for i in range(n):
        integer_list[i] = int(integer_list[i]) # list creation
    t = tuple(integer_list) # convert list to tuple
    print(hash(t))