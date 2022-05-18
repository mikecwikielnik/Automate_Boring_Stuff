"""
birthdays.py.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 113). No Starch Press. Kindle Edition. 
"""

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:   # Pay attn to this loop
        print(birthdays[name] + ' is the birthday of ' + name)
    else:   # Pay attn to this else stmt and the output. 
        print('I do not have bday info for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
            
# This is how you remove mistakes
        
del birthdays['Ski']
del birthdays['birthdays']

birthdays


#######################
# you can the program in the terminal. You typed the below code

# >>> birthdays
# {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'ski': 'jan 8'}
# >>> del birthdays['ski']
# >>> birthdays
# {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# >>>
