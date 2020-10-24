# to convert lower case letter to upper case and vice versa
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    n = str(input("Please input the string: "))
    print(swap_case(n))