"""
List to Dictionary Function for Fantasy Game Inventory
Write a function named addToInventory(inventory, addedItems), 
where the inventory parameter is a dictionary representing the players inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. 
The addToInventory() function should return a dictionary that represents the updated inventory. 
Note that the addedItems list can contain multiples of the same item. Your code could look something like this:

Sweigart, Al. Automate the Boring Stuff with Python, 2nd Edition (p. 128). No Starch Press. Kindle Edition.  
"""

from FantasyGameInventory import displayInventory


def addtoInventory(inventory, addedItems):
    """
    add items to inventory
    """
    for k in addedItems:
        if k not in inventory:
            inventory.setdefault[k, 0]
            inventory[k] = 1
        if k in inventory:
            inventory[k] = inventory[k] + 1

            
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addtoInventory(inv, dragonLoot)

displayInventory(inv)


