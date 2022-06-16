"""
READING AND WRITING FILES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 201). No Starch Press. Kindle Edition. 
"""

from fileinput import hook_encoded
from pathlib import Path

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