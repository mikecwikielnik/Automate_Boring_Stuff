"""
textMyself.py.

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 441). No Starch Press. Kindle Edition. 
"""

#!
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string. 

# Preset values:
accountSID = 'AC123'
authToken = '12345'
myNumber = '+16175554444'
twilioNumber = '+16175559999'

# from twilio.rest import Client

# def textmyself(message):
#     twilioCli = Client(accountSID, authToken)
#     twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)