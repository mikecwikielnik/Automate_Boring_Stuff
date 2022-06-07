"""
CH 7
"""

# Creating Regex Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 165). No Starch Press. Kindle Edition. 

import re

from django.forms import model_to_dict

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

# Optional Matching with the Question Mark

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 168). No Starch Press. Kindle Edition. 

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group()

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group()

# Matching Zero or More with the Star

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 169). No Starch Press. Kindle Edition. 

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

# Matching One or More with the Plus

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 170). No Starch Press. Kindle Edition. 

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()

mo2 = batRegex.search('The Adventures of Batwowowowoman')
mo2.group()

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None

# Matching Specific Repetitions with Braces

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 170). No Starch Press. Kindle Edition. 

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()

mo2 = haRegex.search('Ha')
mo2 == None 

# Greedy and Non-greedy Matching

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 171). No Starch Press. Kindle Edition. 

