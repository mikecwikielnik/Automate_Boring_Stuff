"""
removeCsvHeader.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 378). No Starch Press. Kindle Edition. 
"""

#! 
# removeCsvHeader.py - Removes the header from all csv files in the current
# working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the cwd

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skips non-csv files
    print('Removing header from ' + csvFilename + '...')
    
    # Read the csv file in (skipping first row)
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue    # skip first row
        csvRows.append(row)
    csvFileObj.close()
    
    # Write out the csv file 
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
                      newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()