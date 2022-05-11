"""
Chapter 1: Python Basics
Automate the Boring Stuff, 2nd Edition
Al Sweigart

"""

# Your First Program

# This program says hello and asks for my name

print('Hello World')
print('What is your name?') # ask for their name
myName = input()

print('It is godo to meet you, ' + myName)
print('The length of yoru name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()

print('You will be ' + str(int(myAge)+ 1) + ' in a year.')

# The str(), int(), and float() functions

str(29)

print('I am ' + str(29) + ' years old.')

float(10)