"""
KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 389). No Starch Press. Kindle Edition. 
"""

# The time.time() Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 390). No Starch Press. Kindle Edition. 

import time

time.time()

import time

def calcProd():
    # Calculate the produce of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate' % (endTime - startTime))

import time

time.ctime()
thisMoment = time.time()
time.ctime(thisMoment)

# The time.sleep() Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 391). No Starch Press. Kindle Edition. 

import time

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(2)

