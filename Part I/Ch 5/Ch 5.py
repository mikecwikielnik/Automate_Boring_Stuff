"""
DICTIONARIES AND STRUCTURING DATA

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 111). No Starch Press. Kindle Edition. 
"""

# The dictionary data type

# Key-value pair KVP

from random import sample


myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

myCat['size']
'My cat has ' + myCat['color'] + ' fur.'

# The keys(), values(), and items() Methods

spam = {
    'color': 'red',
    'age': 42
}
for v in spam.values():
    print(v)
    
for k in spam.keys():
    print(k)
    
for i in spam.items():
    print(i)

# If you want to make a list of the keys in a dictionary, this is how:

spam = {
    'color': 'red',
    'age': 42
}
spam.keys()
list(spam.keys())

# Multiple assignment trick

spam = {
    'color': 'red',
    'age': 42
}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
    
# Checking whether a Key or Value exists in a dictionary

spam = {
    'name': 'sophie',
    'age': 7
}
'name' in spam.keys()
'color' not in spam.keys()

# The get() Method

picnicItems = {
    'apples': 5,
    'cups': 2
}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'

# The setdefault() Method

spam = {
    'name': 'Pooka',
    'age': 5
}
if 'color' not in spam: # add the below key, value
    spam['color'] = 'black'

spam.setdefault('color', 'green')

# Nested dictioinaries and lists

allGuests = {
    'Alice': {
        'apples': 5,
        'pretzels': 12
    },
    'Bob': {
        'sandwiches': 3,
        'apples': 2
    },
    'Carol': {
        'cups': 3,
        'apple pies': 1
    }
}
def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples        ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups          ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes         ' + str(totalBrought(allGuests, 'cakes')))
print(' - Sandwiches    ' + str(totalBrought(allGuests, 'sandwiches')))
print(' - Apple Pies    ' + str(totalBrought(allGuests, 'apple pies')))