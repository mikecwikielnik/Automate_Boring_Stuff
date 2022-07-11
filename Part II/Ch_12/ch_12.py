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

# Parsing HTML with the bs4 Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 279). No Starch Press. Kindle Edition. 

import requests, bs4

res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
type(exampleSoup)

# Finding an Element with the select() Method

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 280). No Starch Press. Kindle Edition. 

import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
elems = exampleSoup.select('#author')
type(elems) # elems is a list of Tag objects
len(elems)
type(elems[0])
str(elems[0])   # The Tag object as a string
elems[0].getText()
elems[0].attrs

pElems = exampleSoup.select('p')
str(pElems[0])
pElems[0].getText()
str(pElems[1])
pElems[1].getText()
str(pElems[2])
pElems[2].getText()

# Getting Data from an Element’s Attributes

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 282). No Starch Press. Kindle Edition. 

import bs4

soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
str(spanElem)
spanElem.get('id')
spanElem.get('some_nonexistent_addr') == None
spanElem.attrs

# Starting a selenium-Controlled Browser

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 291). No Starch Press. Kindle Edition. 

from selenium import webdriver

browser = webdriver.Chrome()
type(browser)
browser.get('espn.com')

browser = webdriver.Chrome()
browser.get('espn.com')
try:
    elem = browser.find_element_by_class_name(' cover-thumb')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
    
# Clicking the Page

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 295). No Starch Press. Kindle Edition. 

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('espn.com')
linkElem = browser.find_element_by_link_text('Read Online for Free.')
type(linkElem)

# Filling Out and Submitting Forms

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 295). No Starch Press. Kindle Edition. 

from selenium import webdriver  

browser = webdriver.Chrome()
browser.get('espn.com')
userElem = browser.find_element_by_id('user name')
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('password_here')
passwordElem.submit()

# Sending Special Keys

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 296). No Starch Press. Kindle Edition. 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()
browser.get('espn.com')
htmlElem = browser.find_element_by_tag('html')
htmlElem.send_keys(Keys.END)    # scrolls to bottom
htmlElem.send_keys(Keys.HOME)   # scrolls to top

# Clicking Browser Buttons

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 297). No Starch Press. Kindle Edition. 

browser.back()  # back button
browser.forward()   # forward button
browser.refresh()   # refresh/reload button
browser.quit()  # close button