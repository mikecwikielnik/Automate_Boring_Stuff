"""
Regex Version of the strip() Method 

Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, 
then whitespace characters will be removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 186). No Starch Press. Kindle Edition. 
"""

import re

# sample
spaceRegex = re.compile('\s+')
spaceRegex.sub('**', '   Agent Alice gave away the documents   ')

def spaceReplace(i, n):
    regex = re.compile('\s+')
    southPark=regex.sub(i, n)
    print(southPark)
    
censored = ''
string = ' Cartman says he is going home '

spaceReplace(censored, string) 