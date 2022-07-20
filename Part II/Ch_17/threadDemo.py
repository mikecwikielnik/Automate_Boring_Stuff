"""
threadDemo.py

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 401). No Starch Press. Kindle Edition. 
"""

import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')