"""
validateInput.py:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 137). No Starch Press. Kindle Edition. 
"""

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers')