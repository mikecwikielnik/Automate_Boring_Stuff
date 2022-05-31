""""
MANIPULATING STRINGS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 129). No Starch Press. Kindle Edition. 
"""

# Escape Characters

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 130). No Starch Press. Kindle Edition. 

from http.cookiejar import MozillaCookieJar


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
