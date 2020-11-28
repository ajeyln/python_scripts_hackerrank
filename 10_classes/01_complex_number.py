'''For two complex numbers X and Y, the output should be in the following sequence on separate lines:
X + Y
X - Y
X * Y
X / Y
mod(X)
mod(Y)
For complex numbers with non-zero real(A) and complex part(B), the output should be in the following format:
X+Yi

Replace the plus symbol(+) with a minus symbol (-) when Y<0 .
'''
import math
class Complex(complex):
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))

    def __str__(self):
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
