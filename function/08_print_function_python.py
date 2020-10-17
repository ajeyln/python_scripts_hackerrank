"""The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
123....n"""

from __future__ import print_function

if __name__ == '__main__':
    n = int(input())
result = ""
for i in range(1,n + 1):
    print(i, end="")
    
# using String method
for i in range(1,n + 1):
    y = str(i)
    result = result + y
    i += 1
print("\n")
print(result)