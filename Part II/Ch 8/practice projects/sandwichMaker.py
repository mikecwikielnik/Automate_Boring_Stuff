"""
Sandwich Maker

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 198). No Starch Press. Kindle Edition. 
"""

from numpy import append
import pyinputplus as pyip

bread = ['wheat', 'white', 'sourdough']
protein = ['chicken', 'turkey', 'ham', 'tofu']
qCheese = 'Do you want cheese?'
cheese = ['cheddar', 'swiss', 'mozzarella']
qToppings = 'Do you want toppings?'
toppings = ['mayo', 'mustard', 'lettuce', 'tomato']
anythingElse = 'Do you want anything else?'
topppingsNoMayo = ['mustard', 'lettuce', 'tomato']
toppingsNoMustard = ['mayo', 'lettuce', 'tomato']
toppingsNoLettuce = ['mayo', 'mustard', 'tomato']
toppingsNoTomato = ['mayo', 'mustard', 'lettuce']
sandwichItems = []
sandwichPricing = {
    'wheat': 1,
    'white': 1,
    'sourdough': 1,
    'chicken': 2,
    'turkey': 2,
    'ham': 2,
    'tofu': 2,
    'cheddar': 1,
    'swiss': 1,
    'mozzarella': 1,
    'mayo': 0.5,
    'mustard': 0.5,
    'lettuce': 0.5,
    'tomato': 0.5
}


def sandwichMaker():
    while True:
        print("Hi, welcome to our sandwich shop!")
        response = pyip.inputMenu(bread)
        if response == 'wheat':
            print('ok, wheat')
            sandwichItems.append(response)
            break
        elif response == 'white':
            print('ok, white')
            sandwichItems.append(response)
            break
        elif response == 'sourdough':
            print('ok, sourdough')
            sandwichItems.append(response)
            break
    while True:
        response = pyip.inputMenu(protein)
        if response == 'chicken':
            print('ok, chicken')
            sandwichItems.append(response)
            break
        elif response == 'turkey':
            print('ok, turkey')
            sandwichItems.append(response)
            break
        elif response == 'ham':
            print('ok, ham')
            sandwichItems.append(response)
            break
        elif response == 'tofu':
            print('ok, tofu')
            sandwichItems.append(response)
            break
    while True:
        response = pyip.inputYesNo(qCheese)
        if response == 'yes':
            i = pyip.inputMenu(cheese)
            if i == 'cheddar':
                print('ok, cheddar')
                sandwichItems.append(i)
                break
            if i == 'swiss':
                print('ok, swiss')
                sandwichItems.append(i)
                break
            if i == 'mozzarella':
                print('ok, mozzarella')
                sandwichItems.append(i)
                break
        if response == 'no':
            print('Ok, no cheese.')
            break
    while True:
        response = pyip.inputYesNo(qToppings)
        if response == 'yes':
            i = pyip.inputMenu(toppings)
            if i == 'mayo':
                print('ok, mayo.')
                sandwichItems.append(i)
                response == pyip.inputYesNo(anythingElse)
                if response == 'yes':
                    i = pyip.inputMenu(topppingsNoMayo)
                    if i == 'mustard':
                        print('ok, mustard')
                        sandwichItems.append(i)
                        break
                    if i == 'lettuce':
                        print('ok, lettuce')
                        sandwichItems.append(i)
                        break
                    if i == 'tomato':
                        print('ok, tomato')
                        sandwichItems.append(i)
                        break
                if response == 'no':
                    print('ok.')
                    break
            if i == 'mustard':
                print('ok, mustard')
                sandwichItems.append(i)
                response == pyip.inputYesNo(anythingElse)
                if response == 'yes':
                    i = pyip.inputMenu(toppingsNoMustard)
                    if i == 'mayo':
                        print('ok, mayo')
                        sandwichItems.append(i)
                        break
                    if i == 'lettuce':
                        print('ok, lettuce')
                        sandwichItems.append(i)
                        break
                    if i == 'tomato':
                        print('ok, tomato')
                        sandwichItems.append(i)
                        break
                if response == 'no':
                    print('ok.')
                    break 
            if i == 'lettuce':
                print('ok, lettuce')
                sandwichItems.append(i)
                response == pyip.inputYesNo(anythingElse)
                if response == 'yes':
                    i = pyip.inputMenu(toppingsNoLettuce)
                    if i == 'mayo':
                        print('ok, mayo')
                        sandwichItems.append(i)
                        break
                    if i == 'mustard':
                        print('ok, mustard')
                        sandwichItems.append(i)
                        break
                    if i == 'tomato':
                        print('ok, tomato')
                        sandwichItems.append(i)
                        break
                if response == 'no':
                    print('ok.')
                    break
            if i == 'tomato':
                print('ok, tomato')
                sandwichItems.append(i)
                response == pyip.inputYesNo(anythingElse)
                if response == 'yes':
                    i = pyip.inputMenu(toppingsNoTomato)
                    if i == 'mayo':
                        print('ok, mayo')
                        sandwichItems.append(i)
                        break
                    if i == 'mustard':
                        print('ok, mustard')
                        sandwichItems.append(i)
                        break
                    if i == 'lettuce':
                        print('ok, lettuce')
                        sandwichItems.append(i)
                        break
                if response == 'no':
                    print('ok.')
                    break
        if response == 'no':
            print('ok, no toppings')
            break
        

            
sandwichMaker()

print(sandwichItems)


