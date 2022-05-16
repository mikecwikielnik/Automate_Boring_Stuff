"""
sameNameLocalGlobal.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 69). No Starch Press. Kindle Edition. 
"""

def spam():
    global eggs 
    eggs = 'spam'   # this is the global
    
def bacon():
    eggs = 'bacon'  # this is the local
    
def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)