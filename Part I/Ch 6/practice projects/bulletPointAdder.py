"""
bulletPointAdder.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 147). No Starch Press. Kindle Edition. 
"""

#! python 3
# bulletPointAdder.py - Adds wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)

pyperclip.copy(text)