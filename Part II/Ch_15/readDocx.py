"""
readDocx.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 360). No Starch Press. Kindle Edition. 
"""

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

