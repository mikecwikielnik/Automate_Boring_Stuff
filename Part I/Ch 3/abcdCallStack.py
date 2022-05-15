"""
The Call Stack

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 63). No Starch Press. Kindle Edition. 
"""

def a():
    print('a() starts')
    b() 
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('d() starts')
    print('d() returns')
    
a()
    