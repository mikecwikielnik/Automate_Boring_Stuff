"""
zeroDivide.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 71). No Starch Press. Kindle Edition. 
"""

def spam(divideBy):
    return 42 / divideBy

try:  
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Argument')
