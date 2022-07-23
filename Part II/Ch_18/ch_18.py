"""
SENDING EMAIL AND TEXT MESSAGES

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 415). No Starch Press. Kindle Edition. 
"""

from concurrent.futures import thread
from email import message, message_from_string
from email.errors import MessageParseError
from email.headerregistry import UniqueAddressHeader
from multiprocessing.spawn import import_main_path
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

# Connecting to an IMAP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 425). No Starch Press. Kindle Edition. 

import imapclient

imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)

# Logging In to the IMAP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 426). No Starch Press. Kindle Edition. 

imapObj.login('none@none.com', 'password')

# Searching for Email

# Selecting a Folder

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 426). No Starch Press. Kindle Edition. 

import pprint
pprint.pprint(imapObj.list_folders())

imapObj.select_folder('INBOX', readonly=True)

# Performing the Search

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 427). No Starch Press. Kindle Edition. 

UIDs = imapObj.search(['SINCE 05-Jul-2019'])
UIDs

# Size Limits

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 429). No Starch Press. Kindle Edition. 

import imaplib

imaplib._MAXLINE = 10000000

# Fetching an Email and Marking It as Read

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 430). No Starch Press. Kindle Edition. 

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
import pprint
pprint.pprint(rawMessages)

# Getting Email Addresses from a Raw Message

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 431). No Starch Press. Kindle Edition. 

# import pyzmail
# message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])

message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('cc')
message.get_addresses('bcc')

# Getting the Body from a Raw Message

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 431). No Starch Press. Kindle Edition. 

message.text_part != None
message.text_part.get_payload().decode(message.text_part.charset)
message.html_part != None
message.html_part.get_payload().decode(message.html_part.charset)

# Deleting Emails

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 432). No Starch Press. Kindle Edition. 

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2019'])
UIDs
imapObj.delete_messages(UIDs)
imapObj.expunge()

# Disconnecting from the IMAP Server

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 433). No Starch Press. Kindle Edition. 

imapObj.logout()

# Sending Text Messages

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 439). No Starch Press. Kindle Edition. 

# from twilio.rest import Client  

# accountSID = 'AC123'
# authToken = '1234'
# twilioCli = Client(accountSID, authToken)
# myTwilioNumber = '+16175550123'
# myCellPhone = '+16175558888'
# message = twilioCli.messages.create(body='10 percent off a 3-pair package.', from_=myTwilioNumber, to=myCellPhone)


message.to
message.from_ 
message.body

message.status
message.date_created
message.date_sent == None

message.sid
# updatedMessage = twilioCli.messages.get(message.sid)
# updatedMessage.status
# updatedMessage.date_sent

