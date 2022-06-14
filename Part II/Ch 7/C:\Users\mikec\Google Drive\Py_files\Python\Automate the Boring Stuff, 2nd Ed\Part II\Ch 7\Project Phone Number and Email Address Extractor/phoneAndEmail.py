"""
phoneAndEmail.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 180). No Starch Press. Kindle Edition. 
"""

# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

from ast import MatchClass
from selectors import EpollSelector
from tokenize import group
import pyperclip, re

phoneRegex = re.compile(r'''(
    (\{d}|\(\d{3}\))?               # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# Create email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # at symbol
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text

text = str(pyperclip.paste())       # this is the code that puts the browser text into strings

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if group[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy Results to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')


