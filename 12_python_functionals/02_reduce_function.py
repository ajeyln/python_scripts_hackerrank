# Task
''' To find the product of given rational numbers.'''

#Input
'''First line contains n, the number of rational numbers.
The ith of next n lines contain two integers each, 
the numerator( Ni ) and denominator( Di ) of the ith rational number in the list.'''

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    list1 = []
    for p in range(int(input())):
        list1.append(Fraction(*map(int, input().split())))
    result = product(list1)
    print(*result)