inventory = {'arrow': 12, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory(num_items):
    print('Inventory:')
    count = 0
    for k, v in num_items.items():
        count += v
        print(str(v) + ' ' + k)
        c = count
    print('Total number of items are :' + str(c))


display_inventory(inventory)


def addToInventory(inv, addedItems):
    for i in addedItems:
        if i in inv:
            inv[i] = inv[i] + 1
        else:
            inv[i] = 1
    return inv


inventories = addToInventory(inventory, dragonLoot)
display_inventory(inventories)
