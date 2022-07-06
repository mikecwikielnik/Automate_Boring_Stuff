"""
Chapter 12: WEB SCRAPING

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 267). No Starch Press. Kindle Edition. 
"""

# Downloading a Web Page with the requests.get() Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 271). No Starch Press. Kindle Edition. 

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])

# Checking for Errors

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 272). No Starch Press. Kindle Edition. 

res = requests.get('https://inventwithpython.com/page_doesnt_exist')
res.raise_for_status()

# Always call raise_for_status() after calling requests.get(). 

# You want to be sure that the download has actually worked before your program continues.

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 273). No Starch Press. Kindle Edition. 

# Saving Downloaded Files to the Hard Drive

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 273). No Starch Press. Kindle Edition. 

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()