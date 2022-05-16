"""
Local and Global Variables with the Same Name

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 
"""

def spam():
    eggs = 'spam local'
    print(eggs) # Prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs) # Prints 'bacon local'
    spam()
    print(eggs) # Prints 'bacon local'
    
eggs = 'global'
bacon()
print(eggs)
    
    
# This is a lesson in naming your variables correctly
