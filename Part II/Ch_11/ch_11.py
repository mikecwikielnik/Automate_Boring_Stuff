"""
DEBUGGING

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 249). No Starch Press. Kindle Edition. 
"""

# Assertions

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 253). No Starch Press. Kindle Edition. 

from matplotlib.pyplot import switch_backend


ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
ages
assert ages[0] <= ages[-1]

ages.reverse
ages
assert ages[-1] <= ages[0]

# Using an Assertion in a Traffic Light Simulation

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 254). No Starch Press. Kindle Edition. 

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
            
switchLights(market_2nd)

# You got the right error which helps the program fail early
# thus saving time on debugging

# Logging 

# Using the logging Module

# Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 256). No Starch Press. Kindle Edition. 

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(leveltime)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')