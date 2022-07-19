"""
WORKING WITH CSV FILES AND JSON DATA

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 371). No Starch Press. Kindle Edition. 
"""

# The csv Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 372). No Starch Press. Kindle Edition. 

# reader Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 373). No Starch Press. Kindle Edition. 

import csv
from hashlib import new

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
    
# writer Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 374). No Starch Press. Kindle Edition. 

import csv

outputFile = open('output.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1,2,3.141592,4])
outputFile.close()

# The delimiter and lineterminator Keyword Arguments

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 375). No Starch Press. Kindle Edition. 

import csv

csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()

# With Headers

import csv

exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:
    print(row['Timestamp'], row['Fruit'], row['Quantity'])

# Without Header names

import csv

exampleFile = open('example.csv')
exampleDictReader = csv.DictReader(exampleFile, ['time', 'name',
                                                 'amount'])
for row in exampleDictReader:
    print(row['time'], row['name'], row['amount'])
    
import csv

outputFile = open('output.csv', 'w', newline='')
outputDictWriter = csv.DictWriter(outputFile, ['Name', 'Pet', 'Phone'])
outputDictWriter.writeheader()
outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone':'555-1234'})
outputDictWriter.writerow({'Name': 'bob', 'Phone': '555-9999'})
outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet': 'dog'})
outputFile.close()