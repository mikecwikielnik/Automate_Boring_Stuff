"""
isPhoneNumber.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 162). No Starch Press. Kindle Edition. 
"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(9, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 617-555-8786 tomorrow. 617-555-8786 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')