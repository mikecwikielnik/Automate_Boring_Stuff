"""
sameNameError.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 70). No Starch Press. Kindle Edition. 
"""

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
    
eggs = 'global'
spam()