"""
WORKING WITH PDF AND WORD DOCUMENTS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 347). No Starch Press. Kindle Edition. 
"""

# Extracting Text from PDFs

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 348). No Starch Press. Kindle Edition. 

import PyPDF2
import pyparsing

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
pdfFileObj.close()

# Decrypting PDFs

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 349). No Starch Press. Kindle Edition. 

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted
pdfReader.getPage(0)
pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.decrypt('password')
pageObj = pdfReader.getPage(0)

# Copying Pages

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 351). No Starch Press. Kindle Edition. 

import PyPDF2

pdf1File = open('meetingminutes.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
pdfOutputFile = open('combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()
pdf2File.close()

# Rotating Pages

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 352). No Starch Press. Kindle Edition. 

import PyPDF2

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
page = pdfReader.getPage(0)
page.rotateClockwise(90)
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resultsPdfFile = open('rotatedPage.pdf', 'wb')
pdfWriter.write(resultsPdfFile)
resultsPdfFile.close()
minutesFile.close()

# Overlaying Pages

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 353). No Starch Press. Kindle Edition. 

import PyPDF2
minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
    
resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()

