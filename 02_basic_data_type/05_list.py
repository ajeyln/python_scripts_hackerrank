# write a script to perform the following commands in list:
'''
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''

if __name__ == "__main__":
    n = int(input()) # number of the commands
    list1 = [] # list intalization
    for i in range(n):
        sp = input().split() # spliting of input
        cmd = sp[0] # commands i.e insert,append etc
        args = sp[1:]
        if cmd != "print":
            cmd += "("+",".join(args) +")"
            eval("list1." + cmd)
        else:
            print(list1)
