"""
picnicTable.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 141). No Starch Press. Kindle Edition. 
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        
picnicItems = {
    'sandwiches': 4,
    'apples': 12,
    'cups':4,
    'cookies': 8000
    }
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
