"""
Project: Opening All Search Results

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 283). No Starch Press. Kindle Edition. 
"""

# searchpypi.py - Opens several searcch results

import requests, sys, webbrowser, bs4

print('Searching...')   # display text while downloading the search result page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search?q='
                   + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open a browser tab for each result

linkElems = soup.select('.package-snippet')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
    
    