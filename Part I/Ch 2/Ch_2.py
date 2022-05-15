"""
Chapter 2: Flow Control
Automate the Boring Stuff, 2nd Edition
Al Sweigart

"""

# Boolean Values

from socket import IPV6_UNICAST_HOPS


spam = True
spam


42 == 42

2 != 2

# Blocks of code

name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted. ')
        
# if statements

if name == 'alice':
    print('Hi, allice')
    
# else statements 

if name == 'alice':
    print('hi, alice')
else: 
    print('hello, stranger')
    
# elif statements

age = 5
if name == 'alice':
    print('hi, alice')
elif age < 12:
    print('you are not alice, kiddo')
    
name = 'carol'
age = 3000
if name == 'alice':
    print('hi, alice')
elif age < 12:
    print('you are a kid')
elif age > 2000:
    print('unlike you, alice is not a vampire')
elif age > 100:
    print('you are not alice, granny')

# while loop

spam = 0 
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
    
# an annoying while loop

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('thank you! ')

# break statements

while True:
    print('please type your name')
    name = input()
    if name == 'your name':
        break
print('thank you!')

# continue statements

while True:
    print('who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('hello joe, what is the password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('access granted')

# for loops and the range(function)

print('my name is')
for i in range(5):
    print('555 (' + str(i) + ')')
    
# Gaussian loop

total = 0
for num in range(101):
    total = total + num
print(total)


# an equivalent while loop

print('my name is')
i = 0
while i < 5:
    print('555 (' + str(i) + ')')
    i = i + 1

# The startin, stopping, and stepping arguments to range()

for i in range(12, 16):
    print(i)
    
for i in range(5, -15, -1):
    print(i)
    
# importing modules

import random

for i in range(5):
    print(random.randint(1,10))
    
# Ending a program early with the sys.exit() fn

import sys

while True:
    print('type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + '.')