"""
The Collatz Sequence

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 76). No Starch Press. Kindle Edition. 
"""

def collatz(n):
    list = []
    i = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            print("This number is even")
            list.append(n)
            i += 1
        elif n % 2 == 1:
            n = 3 * n + 1
            print("This number is odd.")
            list.append(n)
            i += 1
    
    print(list)
    
    
collatz(3)

