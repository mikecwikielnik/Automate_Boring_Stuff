"""
convertWordToPDF.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 367). No Starch Press. Kindle Edition. 
"""

# Creating PDFs from Word Documents

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 367). No Starch Press. Kindle Edition. 

# This script runs on Windows only, and you must have Word installed

import win32com.client  # install with "pip install pywin32==224"
import docx

wordFilename = 'your_word_document.docx'
pdfFilename = 'your_pdf_filename.pdf'

doc = docx.Document()
# Code to create Word document goes here
doc.save(wordFilename)

wdFormatPDF = 17    # Word's numeric code for PDFs
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()