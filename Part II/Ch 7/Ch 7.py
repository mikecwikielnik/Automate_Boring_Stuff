"""
CH 7

Pattern Matching with RegEx
"""

# Creating Regex Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 165). No Starch Press. Kindle Edition. 

import re
from tkinter.messagebox import NO

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

# Greedy

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

# The findall() Method

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 171). No Starch Press. Kindle Edition. 

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-2222')
mo.group()

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')   # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-2222')

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 412-555-9999 Work: 212-555-2222')

# Character Classes

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 172). No Starch Press. Kindle Edition. 

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# Making Your Own Character Classes

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 173). No Starch Press. Kindle Edition. 

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. Baby Food.')

consonantRegex = re.compile(r'[^aeiouAEIOU]')   # Negative Character Class
consonantRegex.findall('RoboCop eats baby food. Baby Food.')

# The Caret and Dollar Sign Characters

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 174). No Starch Press. Kindle Edition. 

beginsWithHello = re.compile(r'Hello')
beginsWithHello.search('Hello, world!')
beginsWithHello.search('He said hello') == None

endswithNumber = re.compile('r\d$')
endswithNumber.search('Your number is 42')
endswithNumber.search('Your number is forty two.') == None

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('1234567890')
wholeStringIsNum.search('12345xyz67890') == None
wholeStringIsNum.search('12 34567890') == None

# The Wildcard Character

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 175). No Starch Press. Kindle Edition. 

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')

# Matching Everything with Dot-Star

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 175). No Starch Press. Kindle Edition. 

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)

nongreedyHaRegex = re.compile(r'<.*?>')
mo = nongreedyHaRegex.search('<To serve man> for dinner.>')
mo.group()

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
mo.group()

# Matching Newlines with the Dot Character

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 176). No Starch Press. Kindle Edition. 

noNewlineRegex = re.compile('.*')
noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# Case-Insensitive Matching

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 177). No Starch Press. Kindle Edition. 

robocop = re.compile(r'robocop', re.I)
robocop.search('RoboCop is part man, part machine, all cop.').group()
robocop.search('ROBOCOP protects the innocent.').group()
robocop.search('Al, why does your programming book talk about robocop so much?').group()

# Substituting Strings with the sub() Method

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 178). No Starch Press. Kindle Edition. 

namesRegex =  re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

agentNamesRegex = re.compile(r'Agent (\w)\w*')
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Karen that Agent Eve knew Agent Bob was a double agent.')

# Managing Complex Regexes

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 178). No Starch Press. Kindle Edition. 

phoneRegex = re.compile(r'''(
    (\d{3}|\(\{3}\))?
    (\s|-|\.)?
    \d{3}
    (\s|-|\.)
    \d{4}
    (\s*(ext|x|ext.)\s*\d{2,5})?
    )''', re.VERBOSE)

# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 179). No Starch Press. Kindle Edition. 

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)