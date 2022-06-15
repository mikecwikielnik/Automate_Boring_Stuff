"""
Sandwich Maker

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 198). No Starch Press. Kindle Edition. 
"""

import pyinputplus as pyip

question = 'What type of bread would you like? We have wheat, white, or sourdough.'
bread = ['wheat', 'white', 'sourdough']
protein = ['chicken', 'turkey', 'ham', 'tofu']

def sandwichMaker():
    while True:
        response = pyip.inputMenu(bread)
        if response == 'wheat':
            print('ok, wheat')
            break
        elif response == 'white':
            print('ok, white')
            break
        elif response == 'sourdough':
            print('ok, sourdough')
            break
    while True:
        response = pyip.inputMenu(protein)
        if response == 'chicken':
            print('ok, chicken')
            break
        elif response == 'turkey':
            print('ok, turkey')
            break
        elif response == 'ham':
            print('ok, ham')
            break
        elif response == 'tofu':
            print('ok, tofu')
            break
            
sandwichMaker()


