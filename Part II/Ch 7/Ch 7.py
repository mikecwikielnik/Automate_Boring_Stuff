"""
CH 7
"""

# Creating Regex Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 165). No Starch Press. Kindle Edition. 

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

# Grouping with Parentheses

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 166). No Starch Press. Kindle Edition. 

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(3)
mo.group(0)
mo.groups()

areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
mo.group(2)

# Matching Multiple Groups with the Pipe

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 168). No Starch Press. Kindle Edition. 

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()

mo2 = heroRegex.search('Tina Fey and Batman')
mo2.group()

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()
mo.group(1)