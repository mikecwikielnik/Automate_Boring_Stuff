"""
Project: mapIt.py with the webbrowser Module

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 268). No Starch Press. Kindle Edition. 
"""

# mapIt.py - Launches a map in the browser using an address from the 
# command line or clipboard

# If you have copied 9 southview St Boston, Ma 02125
# this program will yield the google maps page for the above address

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard 
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)