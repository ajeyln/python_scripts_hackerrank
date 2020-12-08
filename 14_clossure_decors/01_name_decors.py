#Task
'''You are given some information about N people. Each person has a first name, last name, age and sex.
 Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. 
 For two people of the same age, print them in the order of their input. '''

# Input Format
'''The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.'''

import operator

def age(x):
    return int(x[2])

def person_lister(f):
    def inner(people):
        return map(f,sorted(people, key=age))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')