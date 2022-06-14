"""
INPUT VALIDATION

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 187). No Starch Press. Kindle Edition. 
"""

while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
    print(f"Your age is {age}")
    break


from numpy import block
import pyinputplus as pyip

response = pyip.inputNum()

response = input('Enter a number: ')
response

response = pyip.inputInt(prompt='Enter a number: ')
response

# The min, max, greaterThan, and lessThan Keyword Arguments

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 190). No Starch Press. Kindle Edition. 

import pyinputplus as pyip

response = pyip.inputNum('Enter num: ', min=4)
response

response = pyip.inputNum('Enter num: ', greaterThan=4)
response

response = pyip.inputNum('>', min=4, lessThan=6)
response

# The blank Keyword Argument

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 191). No Starch Press. Kindle Edition. 

import pyinputplus as pyip

response = pyip.inputNum('Enter num: ')
response

response = pyip.inputNum(blank=True)
response 

# The limit, timeout, and default Keyword Arguments

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 191). No Starch Press. Kindle Edition. 

import pyinputplus as pyip

response = pyip.inputNum(limit=2)

response = pyip.inputNum(timeout=10)

response = pyip.inputNum(limit=2, default='N/A')

# The allowRegexes and blockRegexes Keyword Arguments

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 192). No Starch Press. Kindle Edition. 

import pyinputplus as pyip

response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response

response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
response

import pyinputplus as pyip

response = pyip.inputNum(blockRegexes=[r'[02468]$'])
response

import pyinputplus as pyip

response = pyip.inputStr(allowRegexes=[r'caterpillar', 'category'],
                         blockRegexes=[r'cat'])
response