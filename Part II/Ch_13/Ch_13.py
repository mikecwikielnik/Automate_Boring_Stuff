"""
WORKING WITH EXCEL SPREADSHEETS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 301). No Starch Press. Kindle Edition. 
"""

import openpyxl

# Opening Excel Documents with OpenPyXL

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 303). No Starch Press. Kindle Edition. 

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
type(wb)

# Getting Sheets from the Workbook

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 304). No Starch Press. Kindle Edition. 

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
wb.sheetnames   # the workbook's sheets' names
sheet = wb['Sheet3']    # get a sheet from the workbook
sheet
type(sheet)
sheet.title # Get the sheet's title as a string
anotherSheet = wb.active    # Get the active sheet
anotherSheet

# Getting Cells from the Sheets

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 304). No Starch Press. Kindle Edition. 

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']    # Get the sheet
sheet['A1'] # Get the cell from the sheet
sheet['A1'].value   # Get the value
c = sheet['B1'] # Get another cell from the sheet
c.value
'Row %s, Column %s is %s' % (c.row, c.column, c.value)
'Cell %s is %s' % (c.coordinate, c.value)
sheet['C1'].value

sheet.cell(row=1, column=2)
sheet.cell(row=1, column=2).value
for i in range(1, 8, 2):    # Go through every other row:
    print(i, sheet.cell(row=i, column=2).value)

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
sheet.max_row   # Get the highest row number
sheet.max_column    # Get the highest column number NOTE: it is a number, not a letter

# Converting Between Column Letters and Numbers

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 306). No Starch Press. Kindle Edition. 

import openpyxl

from openpyxl.utils import get_column_letter, column_index_from_string

get_column_letter(2)
get_column_letter(27)
get_column_letter(1900)
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
get_column_letter(sheet.max_column)
column_index_from_string('A')   # Get A's number
column_index_from_string('ZZZ')

# Getting Rows and Columns from the Sheets

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 306). No Starch Press. Kindle Edition. 

import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
tuple(sheet['A1':'C3']) # Get all cells from A1 to C3
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
    
import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
list(sheet.columns)[1]
for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)
    
