'''You are given a date. Your task is to find what the day is on that date.'''
#Input Format

'''A single line of input containing the space separated month, day and year, respectively, in DD/MM/YYYY format.'''

import calendar
dd,mm,yyyy=map(int,input("Enter a date(dd mm yyyy format):\n").split())
print((calendar.day_name[calendar.weekday(yyyy,mm,dd)]).upper())