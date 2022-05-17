"""
Magic 8 Ball with a List

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 92). No Starch Press. Kindle Edition. 
"""

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

# This produces a random number to use for the index, regardless of the size of messages. 
# That is, you’ll get a random number between 0 and the value of len(messages) - 1.
# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 93). No Starch Press. Kindle Edition. 

print(messages[random.randint(0, len(messages) - 1)])

# len () Seems to always provide the n value of a list. 
# This is valuable because you might need to change the size of the list at different points in a program. 

len(messages)   


