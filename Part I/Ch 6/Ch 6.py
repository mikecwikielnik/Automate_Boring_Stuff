""""
MANIPULATING STRINGS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 129). No Starch Press. Kindle Edition. 
"""

# Escape Characters

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 130). No Starch Press. Kindle Edition. 

from http.cookiejar import MozillaCookieJar
from sys import pycache_prefix


print("Hello there!\nHow are you?\nI\'m doing fine. ")

# Raw Strings

# Raw strings are helpful if you are typing string values that contain many backslashes, 
# such as the strings used for Windows file paths like r'C:\Users\Al\Desktop' 
# or regular expressions described in the next chapter.

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 131). No Starch Press. Kindle Edition. 

print(r'That is Carol\'s cat.')

# Putting Strings Inside Other Strings

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 134). No Starch Press. Kindle Edition. 

# exactly like print(f"{string}")
name = 'Mike'
age = 4000
'My name is %s. I am %s years old.' % (name, age)

f'My name is {name}, and next year, I will be {age +1}'

# The join() and split() Methods

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 138). No Starch Press. Kindle Edition. 

a = ','.join(['cats', 'rats', 'bats'])

a.split()

'My name is mike'.split()

'My name is Mike'.split('M')

spam = '''Dear Alice,  
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''

spam.split('\n')    # This will probably be super useful one day 

# Splitting Strings with the partition() Method

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 140). No Starch Press. Kindle Edition. 

'Hello, world!'.partition('w')
'Hello, world!'.partition('world')  # ('before', 'what u want', 'after')
'Hello, world!'.partition('o')  # first occurence only
'Hello, world!'.partition('xyz')    # returns nothing
before, sep, after = 'Hello, world!'.partition(' ')
before
sep
after   #The partition() method is useful for splitting a string whenever you need the parts before, including, and after a particular separator string.

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 140). No Starch Press. Kindle Edition. 

# Justifying Text with the rjust(), ljust(), and center() Methods

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 140). No Starch Press. Kindle Edition. 

'Hello'.rjust(10)

'Hello, World!'.ljust(20)

'Hello'.rjust(20, '*')

'Whats up people!?'.center(35, '^')


# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 142). No Starch Press. Kindle Edition. 

spam = '     Hello, world     '
spam.strip()
spam.lstrip()
spam.rstrip()

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

# Numeric Values of Characters with the ord() and chr() Functions

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 143). No Starch Press. Kindle Edition. 

ord('A')
ord('4')
ord('!')
chr(65)

ord('A') < ord('B')
chr(ord('A'))
chr(ord('A')+1)

# Copying and Pasting Strings with the pyperclip Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 143). No Starch Press. Kindle Edition. 

import pyperclip

pyperclip.copy('Hello World!')
pyperclip.paste()