"""
Project Combining Select Pages from Many PDFs

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 355). No Starch Press. Kindle Edition. 
"""

# combinePdfs.py - Combines all the PDFs in the cwd into 
# into a single PDF

import PyPDF2, os
# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # TODO: Loop through all the pages (except the first) and add them

# TODO: Save the resulting PDF to a file 
