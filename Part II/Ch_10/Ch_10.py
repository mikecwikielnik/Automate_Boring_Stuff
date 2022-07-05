"""
ORGANIZING FILES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 231). No Starch Press. Kindle Edition. 
"""

# The shutil Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 232). No Starch Press. Kindle Edition. 

# The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 232). No Starch Press. Kindle Edition. 

# Copying Files and Folders

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 232). No Starch Press. Kindle Edition. 

from doctest import Example
import imp
import shutil, os
from pathlib import Path

p = Path.home()
shutil.copy(p / 'eggs.txt', p / 'some_folder')
shutil.copy(p / 'eggs.txt', p / 'some_folder/egg2.txt')

shutil.copytree(p / 'spam', p / 'spam_backup')

# Moving and Renaming Files and Folders

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 233). No Starch Press. Kindle Edition. 

import shutil

shutil.move('C:\\bacon.txt', 'C;\\eggs')

# Permanently Deleting Files and Folders

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 234). No Starch Press. Kindle Edition. 

import os
from pathlib import Path
for filename in Path.home().glob('*.rxt'):
    # os.unlink(filename)
    print(filename)
    
# Safe Deletes with the send2trash Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 235). No Starch Press. Kindle Edition. 

# import send2trash

baconFile = open('bacon.txt', 'a')  # Creates the file
baconFile.write('Bacon is not a vegetable')
baconFile.close()
# send2trash.send2trash('bacon.txt')

# Walking a Directory Tree

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 235). No Starch Press. Kindle Edition. 

import os

for folderName, subfolders, filenames in os.walk('C:\\delicious'):
    print('The current folder is ' + folderName)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': ' + filename)
        
    print('')
    
# Reading ZIP Files

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 238). No Starch Press. Kindle Edition. 

import zipfile, os
from pathlib import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!'
exampleZip.close()

# Extracting from ZIP Files

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 238). No Starch Press. Kindle Edition. 

import zipfile, os
from pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall()
exampleZip.close()

exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
exampleZip.close()

# Creating and Adding to ZIP Files

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 239). No Starch Press. Kindle Edition. 

import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()

