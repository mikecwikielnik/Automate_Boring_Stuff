"""
KEEPING TIME, SCHEDULING TASKS, AND LAUNCHING PROGRAMS

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 389). No Starch Press. Kindle Edition. 
"""

# The time.time() Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 390). No Starch Press. Kindle Edition. 

import time

from django.forms import DateInput

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

# Rounding Numbers

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 392). No Starch Press. Kindle Edition. 

import time

now = time.time()
now
round(now, 2)
round(now, 4)
round(now)

# The datetime Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 395). No Starch Press. Kindle Edition. 

import datetime

datetime.datetime.now()
dt = datetime.datetime(2019, 10, 21, 16, 29, 0)
dt.year, dt.month, dt.day
dt.hour, dt.minute, dt.second

import datetime, time

datetime.datetime.fromtimestamp(10000)
datetime.datetime.fromtimestamp(time.time())

halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
halloween2019 == oct31_2019
halloween2019 > newyears2020
newyears2020 > halloween2019
newyears2020 != oct31_2019

# The timedelta Data Type

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 396). No Starch Press. Kindle Edition. 

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
delta.days, delta.seconds, delta.microseconds
delta.total_seconds()
str(delta)

dt = datetime.datetime.now()
dt 
thousandDays = datetime.timedelta(days=1000)
dt + thousandDays

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
aboutThirtyYears = datetime.timedelta(days=365 * 30)
oct21st
oct21st - aboutThirtyYears
oct21st - (2 * aboutThirtyYears)

# Pausing Until a Specific Date

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 397). No Starch Press. Kindle Edition. 

import datetime
import time

halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
    
# Converting datetime Objects into Strings

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 398). No Starch Press. Kindle Edition. 

oct21st = datetime.datetime(2019, 10, 21, 16, 29, 0)
oct21st.strftime('%Y/%m/%d %H:%M:%S')
oct21st.strftime('%I:%M %p')
oct21st.strftime("%B of '%y")   # notice small y

# Converting Strings into datetime Objects

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 399). No Starch Press. Kindle Edition. 

datetime.datetime.strptime('October 21, 2019', '%B %d, %Y')
datetime.datetime.strptime('2019/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
datetime.datetime.strptime("October of '19", "%B of '%y")   # notice small y
datetime.datetime.strptime("November of '63", "%B of '%y")

# Passing Arguments to the Thread’s Target Function

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 402). No Starch Press. Kindle Edition. 

print('Cats', 'Dogs', 'Frogs', sep=' & ')

import threading

threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
                             kwargs={'sep': ' & '})
threadObj.start()