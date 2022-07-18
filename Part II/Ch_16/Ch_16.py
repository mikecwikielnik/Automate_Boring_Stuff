"""
WORKING WITH CSV FILES AND JSON DATA

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 371). No Starch Press. Kindle Edition. 
"""

# The csv Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 372). No Starch Press. Kindle Edition. 

# reader Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 373). No Starch Press. Kindle Edition. 

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
exampleData

# Accessing the lists inside the bigger list

exampleData[0][0]
exampleData[0][1]
exampleData[0][2]
exampleData[1][1]
exampleData[6][1]

# Reading Data from reader Objects in a for Loop

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 374). No Starch Press. Kindle Edition. 

import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    
