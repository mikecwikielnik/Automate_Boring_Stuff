# This is a guess the number game

import random

secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# Ask the player to guess 6 times.

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())    # good to know
    
    if guess < secretNumber:
        print('guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break   # this condition is the correct guess!
    
if guess == secretNumber:
    print('good job! you guessed my number ' + str(guessesTaken) + ' guesses!')
else: 
    print('nope, i was thinking of ' + str(secretNumber))