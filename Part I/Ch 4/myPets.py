"""
myPets.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 85). No Starch Press. Kindle Edition. 
"""

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I dont have a pet named ' + name)
else:
    print(name + ' is my pet.')