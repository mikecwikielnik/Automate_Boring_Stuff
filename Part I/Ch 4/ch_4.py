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

# Sequence Data Types

name = 'sophie'

name[0]

name[-2]

name[0:4]

'so' in name

'm' in name

'p' not in name

for i in name:
    print('***' + i + '***')
    
# Mutable and Immutable Data Types

# The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string.

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 94). No Starch Press. Kindle Edition. 

name = 'sophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name
newName

# The tupe data type

eggs = ('hello', 42, 0.5)
eggs[0]
eggs[1:3]
len(eggs)

type(('hello',))
type(('hello'))

# Converting types with the list() and tuple() functions

tuple(['cat', 'dog', 5])
list(('cat', 'dog', 5))
list('hello')

# References

spam = [0, 1, 2, 3, 4, 5]
cheese = spam   # The reference is being copied, not the list. 
cheese[1] = 'Hello!'    # This changes the list value
spam
cheese  # The cheese variable refers to the same list

# Identity and the id() function

id('howdy') # The returned number will be different on your machine

bacon = 'Hello'
id(bacon)
bacon += ' world'   # A new string is made from 'Hello' and ' world'.
id(bacon)   # bacon now refers to a completely different string. 

# Modifying the object in-place

eggs = ['cat', 'dog']   # This creates a new list
id(eggs)
eggs.append('moose')    # append() modifies the list "in place"
id(eggs)    # eggs still refers to the same list as before
eggs = ['bat', 'cat', 'cow']    # New list, new identity
id(eggs)    # eggs now refers to a completely different list
