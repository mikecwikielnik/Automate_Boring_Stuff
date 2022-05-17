"""
LISTS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 77). No Starch Press. Kindle Edition. 
"""

# The multiple assignment trick

import enum


cat = ['fat', 'gray', 'loud']
size, color, character = cat 

size

print(color)

# Using the enumerate() Function with dictionaries, i changed from lists

supplies = {"pens":"black",
            "staplers": "brown",
            "flamethrowers":"green", 
            "binders":"red"}
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)   # This is the book
    print(f"This is the better to type: Index {index} in supplies is: {item} ") # You learned this in Crash Course
    
for value in supplies.values():
    print(f"{value}")
    
# Using the random.choice() and random.shuffle() Functions with Lists

import random

pets = ['dog', 'cat', 'moose']
random.choice(pets)

letters = ['x', 'y', 'z', 'a', 'b', 'c']
random.shuffle(letters)

letters

# Augmented Assignment Operators

x = 1

x += 1
x -= 1
x *= 1
x /= 1
x %= 1

x


# Finding a Value in a list with the index() method

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # If there is more than one hello, it returns the first index- thats it. 

# Adding values to lists with append() and insert()

spam.append('moose')

spam.insert(1, 'chicken')

spam

# Removing values 

spam.remove('heyas')

spam

# Sorting values

spam = [random.randint(1,1000), random.randint(1,3),]

spam.sort()
spam 

spam.reverse()
spam 