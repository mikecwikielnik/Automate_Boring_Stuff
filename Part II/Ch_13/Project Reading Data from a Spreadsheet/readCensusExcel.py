"""
readCensusExcel.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 309). No Starch Press. Kindle Edition. 
"""

# readCensusExcel.py - Tabulates population and number of census tracts for 
# each county.

from os import stat
import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

# TODO: Fill in countyData with each county's population and tracts
print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value
    
    # Make sure the key for this state exists
    countyData.setdefault(state, {})
    # Make sure the key for this county in this state exists
    countyData[state].setdefault(county, {'tracts': 0, 'pop':0})
    
    # Each row represents one census tract, so increment by one. 
    countyData[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)
    
# Open a new text file and write the contents of countyData to it. 
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done. ')

import os

import census2010
census2010.allData['AK']['Anchorage']
anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was ' + str(anchoragePop))