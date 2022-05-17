"""
allMyCats2.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 83). No Starch Press. Kindle Edition. 
"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
    
# Run the code separately
    
print('The cat names are:')
for name in catNames:
    print(' ' + name)
    