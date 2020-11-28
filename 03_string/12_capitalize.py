'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, ajey nayak should be capitalised correctly as Ajey Nayak.


Given a full name, your task is to capitalize the name appropriately.'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return s.title()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
