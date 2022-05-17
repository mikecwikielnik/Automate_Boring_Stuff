"""
Coin Flip Streaks

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 107). No Starch Press. Kindle Edition. 
"""

import random

list, heads, tails = [], [], []

for i in range(1000000):
    randNum = random.randint(0,1)
    if randNum == 1:
        list.append(randNum)
        heads.append(randNum)
    elif randNum == 0:
        list.append(randNum)
        tails.append(randNum)

# Getting the totals of heads, tails with the total (range(i))

len(list)
len(heads)
len(tails)

# Calculating the ratio of heads, tails

len(heads)/len(list)
len(tails)/len(list)    

