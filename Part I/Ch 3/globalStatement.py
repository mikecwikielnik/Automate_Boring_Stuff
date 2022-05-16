"""
The global Statement

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 
"""

def spam():
    global eggs 
    eggs = 'spam'
    
eggs = 'global'
spam()
print(eggs)