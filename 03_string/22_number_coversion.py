'''Given an integer,n , print the following values for each integer i from 1 to n :
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
5. The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .'''

def print_formatted(number):
    for i in range(1, number+1):
        print(f'{i:15d} {i:15o} {i:15X} {i:15b}')5
        

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print_formatted(n)