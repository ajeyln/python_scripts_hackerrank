'''ABC is a right triangle, 90 degree at B.
Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find MBC (angle 0 degree) in degrees.'''

from math import *

ab = float(input())
bc = float(input())
print(str(int(round(degrees(atan(ab/bc)),0)))+'°')