#Task
''' Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.'''

# Input Format
''' A single line of input contains the string S.'''

from string import ascii_lowercase, ascii_uppercase 
sortkey = ascii_lowercase + ascii_uppercase + "1357902468"
x = input()
print(*map(lambda y: y * x.count(y), sortkey), sep='')