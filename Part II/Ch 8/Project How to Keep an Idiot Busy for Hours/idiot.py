"""
idiot.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 195). No Starch Press. Kindle Edition. 
"""

import pyinputplus as pyip

while True:
    prompt = 'Want to know how to keep an idiot busy for house?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        print('Thank you. Have a nice day.')
        break
