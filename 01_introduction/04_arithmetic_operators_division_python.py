from __future__ import division

if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    while b != 0:
        print(int(a / b))
        print(float(a / b))
    b = int(input("Enter second number: "))
    print(" Please Enter second number other than zero")