"""
SENDING EMAIL AND TEXT MESSAGES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 415). No Starch Press. Kindle Edition. 
"""

from concurrent.futures import thread
from email import message, message_from_string
from email.headerregistry import UniqueAddressHeader
import ezgmail, os

os.chdir(r'C:\path\to\credentials_json_file')
ezgmail.init()

# Sending Mail from a Gmail Account

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 417). No Starch Press. Kindle Edition. 

import ezgmail

ezgmail.send('none@none.com', 'subject line', 'body of email')
ezgmail.send('none@none.com', 'subject line', 'body of email', ['attachment1.jpg', 'attachment2.jpg'])
ezgmail.send('none@none.com', 'subject line', 'body of email', cc='friend@none.com', bcc='none1@none.com,none2@none.com')

# Reading Mail from a Gmail Account

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 418). No Starch Press. Kindle Edition. 

import ezgmail

unreadThreads = ezgmail.unread()    # List of GmailThrea objects
ezgmail.summary(unreadThreads)

len(unreadThreads)
str(unreadThreads[0])
len(unreadThreads[0].messages)
str(unreadThreads[0].messages[0])
unreadThreads[0].messages[0].subject
unreadThreads[0].messages[0].body
unreadThreads[0].messages[0].timestamp
unreadThreads[0].messages[0].sender
unreadThreads[0].messages[0].recipient 

# Searching Mail from a Gmail Account

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 419). No Starch Press. Kindle Edition. 

resultThreads = ezgmail.search('RoboCop')
len(resultThreads)
ezgmail.summary(resultThreads)

# Downloading Attachments from a Gmail Account

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 419). No Starch Press. Kindle Edition. 

import ezgmail

threads = ezgmail.search('vacation photos')
threads[0].messages[0].attachments
threads[0].messages[0].downloadAttachment('tulips.jpg')
threads[0].messages[0].downloadAttachments(downloadFolder='vacation2019')

# Sending Email

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 420). No Starch Press. Kindle Edition. 

import smtplib

smtpObj = smtplib.SMTP('smtp.example.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('bob@example.com', 'my_secret_password')
smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: so long.\nDear Alice, so long and thanks for all the fish. Best, Bob')
smtpObj.quit()

# Connecting to an SMTP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 421). No Starch Press. Kindle Edition. 

smtpObj - smtplib.SMTP('smtp.example.com', 587)
type(smtpObj)

smtpObj = smtplib.SMTP_SSL('smtp.example.com', 465)

# Sending the SMTP “Hello” Message

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 422). No Starch Press. Kindle Edition. 

smtpObj.ehlo()

# Starting TLS Encryption

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 422). No Starch Press. Kindle Edition. 

smtpObj.starttls()

# Logging In to the SMTP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 423). No Starch Press. Kindle Edition. 

smtpObj.login('email@example.com', 'password')

# Sending an Email

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 423). No Starch Press. Kindle Edition. 

smtpObj.sendmail('email@none.com',
                 'recipient@none.com',
                 'subject: thanks for the help\nBest, Bob')

# Disconnecting from the SMTP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 424). No Starch Press. Kindle Edition. 

smtpObj.quit()

# Retrieving and Deleting Emails with IMAP

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 424). No Starch Press. Kindle Edition. 

import imapclient

imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
imapObj.login('email@none.com', 'password')
imapObj.select_folder('INBOX', readonly=True)
UIDs = imapObj.search(['SINCE 05-Jul-2019'])
UIDs
rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# import pyzmail
# message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
# message.get_subject()
# message.get_addresses('from')
# message.get_addresses('to')
# message.get_addresses('cc')
# message.get_addresses('bcc')
# message.text_part != None
# message.text_part.get_payload().decode(message.text_part.charset)
# message.html_part != None
# message.html_part.get_payload().decode(message.html_part.chartset)
# imapObj.logout()

