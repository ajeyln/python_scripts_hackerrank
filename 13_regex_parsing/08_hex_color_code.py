# Background
'''CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code: '''

# It must start with a '#' symbol.
# It can have 3 or 6 digits.
# Each digit is in the range of 0 to F. (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and f).
# A-F letters can be lower case. (a, b, c, d, e and f are also valid digits).

# Input Format
''' The first line contains N, the number of code lines.
The next N lines contains CSS Codes.'''

import re

for i in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')