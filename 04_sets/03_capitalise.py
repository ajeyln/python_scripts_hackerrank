#!/bin/python3

'''s = input()
d = s.split(" ")
print(d)
l = []
for i in d:
    c = i.capitalize()
    l.append(c)

print(' '.join(l))'''

s = input()
y = s.split()
d = []
for i in y:
    print(i)
    m = i[0].upper() + i[1:].lower()
    d.append(m)
w = " ".join(d)
print (w)

    