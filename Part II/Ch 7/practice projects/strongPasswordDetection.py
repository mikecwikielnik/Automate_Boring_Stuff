"""
Strong Password Detection 

Write a function that uses regular expressions to make sure the password string it is passed is strong. 
A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 186). No Starch Press. Kindle Edition. 
"""

import re

passwordRegex = re.compile(r'''(
    ([a-zA-Z]{8,16})
    ([0-9]{1,16})
)''', re.VERBOSE)

# scrap
# passwordRegex.search('aBcDeFgH0123') 
# passwordRegex.search('xy321') 
# passwordRegex.search('My password is ABCDEFGHIJK01233456') 

def passwordChecker(i):
    if passwordRegex.search(i) == None:
        print("weak password")
    else:
        print("strong password")

password = ('aBcDeFgH0123')
passwordChecker(password)