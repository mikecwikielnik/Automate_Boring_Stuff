"""
READING AND WRITING FILES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 201). No Starch Press. Kindle Edition. 
"""

from fileinput import hook_encoded
from pathlib import Path
from struct import calcsize
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

# Handling Absolute and Relative Paths

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 208). No Starch Press. Kindle Edition. 

Path.cwd()
Path.cwd().is_absolute()
Path('spam/bacon/eggs').is_absolute()

Path('my/relative/path')
Path.cwd()/Path('my/relative/path')

# To get to another folder but starting at the C: 

Path.home()/Path('my/relative/path')

# Getting the Parts of a File Path

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 209). No Starch Press. Kindle Edition. 

p = Path('C:/Users/Al/spam.txt')
p.anchor
p.parent    # This is a Path object, not a string.
p.name
p.stem
p.suffix
p.drive

Path.cwd()
Path.cwd().parents[0]
Path.cwd().parents[2]
Path.cwd().parents[5]



calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(calcFilePath)
os.path.dirname(calcFilePath)

os.path.split(calcFilePath)

(os.path.dirname(calcFilePath), os.path.basename(calcFilePath))

# Returns specific folders

calcFilePath.split(os.sep)

# Finding File Sizes and Folder Contents

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 212). No Starch Press. Kindle Edition. 

os.path.getsize('C:\\Windows\\System32\\calc.exe')

os.listdir('C:\\Windows\\System32')

totalsize = 0

for filename in os.listdir('C:\\Windows\\System32'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalsize)

# Modifying a List of Files Using Glob Patterns

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 213). No Starch Press. Kindle Edition. 

p = Path('c:/Users/mikec/Desktop')
p.glob('*')
list(p.glob('*'))   # Make a list froma the generator

list(p.glob('*.txt'))   # Lists all text files

list(p.glob('*.?x?'))

p = Path('C:/Users/mikec/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj)  # Prints the Path object as a string
    
