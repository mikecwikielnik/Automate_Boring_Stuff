"""
DEBUGGING

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 249). No Starch Press. Kindle Edition. 
"""

# Assertions

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 253). No Starch Press. Kindle Edition. 

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
assert ages[0] <= ages[-1]

ages.reverse
ages
assert ages[-1] <= ages[0]