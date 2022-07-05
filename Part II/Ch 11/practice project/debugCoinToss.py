"""
Debugging Coin Toss

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 266). No Starch Press. Kindle Edition. 
"""

# PRACTICE SCRAP

import random

n = 0
guess = []

while True:
    if n < 5:
        i = random.randint(0,1)
        guess.append(i)
        n += 1
    else:
        break   # Python requires this "else: break" stmt because i guess we haven't defined 
                # what happens when n >= 5. When we define this, we can print the list 'guess'.
                # If you remember, you couldn't print guess. I think that was visual codes hint
                # that this loop will go on forever. 
print(guess)

# PRACTICE PROJECT


import random

while True:
    guess = input()
    toss = random.randint(0,1)
    if str(guess) == str(toss):  # Both guess/toss need to be both str or int but not str/int- forever loop
        print(f"CONGRATS! {guess} equals {toss} !!!!")
        break
    else:
        print(f"whoopsie {guess} doesn't equal {toss}")

