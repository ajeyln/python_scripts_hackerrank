# Task
''' You are given N mobile numbers. Sort them in ascending order then print them in the standard format 
The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number.
Alternatively, there may not be any prefix at all.'''

# Input Format
''' The first line of input contains an integer N, the number of mobile phone numbers.
N lines follow each containing a mobile number.'''

def wrapper(f):
    def fun(l):
        f('+91 {} {}'.format(n[-10:-5], n[-5:]) for n in l)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
