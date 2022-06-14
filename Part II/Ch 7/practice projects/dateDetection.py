"""
Date Detection 

Write a regular expression that can detect dates in the DD/MM/YYYY format. 
Assume that the days range from 01 to 31, the months range from 01 to 12, and the years range from 1000 to 2999. 
Note that if the day or month is a single digit, itll have a leading zero. 
The regular expression doesnt have to detect correct days for each month or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021. 
Then store these strings into variables named month, day, and year, and write additional code that can detect if it is a valid date. 
April, June, September, and November have 30 days, February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. 
Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 

Note how this calculation makes it impossible to make a reasonably sized regular expression that can detect a valid date.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 186). No Starch Press. Kindle Edition. 
"""

import re

# small scratch example

dateRegex = re.compile(r'\d\d/\d\d/\d\d\d\d')
mo = dateRegex.search('Todays date is 06/14/2022')
print('Date found: ' + mo.group())

# grouping with parentheses helps create the m,d,y variables

dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
mo = dateRegex.search('Todays date is 10/11/1990')
mo.group(3)
mo.group(2)
mo.group(1)

month, day, year = mo.groups()
print(month)
print(day)
print(year)

def checkDays(i):
    if i == '04':
        print(f"{i} has only 30 days.")
    elif i == '06':
        print(f"{i} has only 30 days.") 
    elif i == '09':
        print(f"{i} has only 30 days.")
    elif i == '11':
        print(f"{i} has only 30 days.")
    elif i == '02':
        print(f"{i} has only 28 days.")
    else:
        print(f"{i} has 31 days.")

def checkYear(i):
    if int(i) > 1000 and int(i) < 2999:
        print("valid year")
    else:
        print("not a valid year")

checkDays(month)
checkYear(year)