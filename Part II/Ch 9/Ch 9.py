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
    
# The File Reading/Writing Process

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 215). No Starch Press. Kindle Edition. 

from pathlib import Path 

p = Path('spam.txt')    # Path object methods only provide basic methods
p.write_text('hello, world!')
p.read_text()

# Opening Files with the open() Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 217). No Starch Press. Kindle Edition. 

helloFile = open('C:/Users/mikec/Google Drive/Py_files/Python/Automate the Boring Stuff, 2nd Ed/Part II/Ch 9/spam.txt')


# Reading the Contents of Files

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 217). No Starch Press. Kindle Edition. 

helloContent = helloFile.read()
helloContent

# Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text. 

# For example, create a file named sonnet29.txt in the same directory as hello.txt and write the following text in it:

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 218). No Starch Press. Kindle Edition. 

p = Path('sonnet29.txt')
p.write_text('When, in disgrace with fortune and men\'s eyes, I all alone between my outcast state, And trouble deaf heaven with my bootless cries, And look upon myself and curse my fate,')

sonnetFile = open('C:/Users/mikec/Google Drive/Py_files/Python/Automate the Boring Stuff, 2nd Ed/Part II/Ch 9/sonnet29.txt')
sonnetFile.readlines()

# Writing to Files

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 218). No Starch Press. Kindle Edition. 

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')  # append
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)


