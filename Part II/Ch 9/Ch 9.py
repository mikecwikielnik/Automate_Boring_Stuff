"""
READING AND WRITING FILES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 201). No Starch Press. Kindle Edition. 
"""

from fileinput import hook_encoded
from pathlib import Path
from turtle import home

Path('spam', 'bacon', 'eggs')

# Using the / Operator to Join Paths

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 204). No Starch Press. Kindle Edition. 

from pathlib import Path

Path('spam')/'bacon'/'eggs'
Path('spam')/Path('bacon/eggs')
Path('spam')/Path('bacon', 'eggs')

homeFolder = r'C:\Users\mikec'
subFolder = 'spam'
homeFolder + '\\' + subFolder
'\\'.join([homeFolder, subFolder])


homeFolder = Path('C:/Users/mikec')
subFolder = Path('spam')
homeFolder / subFolder
str(homeFolder / subFolder)

# The Current Working Directory

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 205). No Starch Press. Kindle Edition. 

from pathlib import Path

import os

Path.cwd()  # same as os.getcwd()
os.getcwd() # except, os.getcwd() output is a string 

# The Home Directory

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 206). No Starch Press. Kindle Edition. 

Path.home()