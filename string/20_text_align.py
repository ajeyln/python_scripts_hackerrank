# Wrap a string with given paragraph of width 

import textwrap

def wrap(string, max_width):
    print("\n".join(string[i:i+ max_width] for i in range(0, len(string), max_width)))

if __name__ == '__main__':
    string = input("Enter a string: "), 
    max_width = int(input()) # width of string for wrapping
    wrap(string, max_width)