"""
### 4. The E-Commerce Cart-to-Inventory Synchronizer

A checkout system needs to cross-check an order with the store warehouse. Given an inventory dictionary {"item": stock_count} and a customer cart list of tuples (item, requested_qty), loop through the cart, check if the stock is sufficient, and decrement the inventory dict in-place if valid.
"""

inventory = {"apple": 10,
             "banana": 5,
             "orange": 3,
             "milk": 2}

cart = [("apple", 3), ("banana", 6), ("orange", 2), ("milk", 1), ("apple", 2)]

for i,j in cart:
  if i in inventory:
    if j<= inventory[i]:
      inventory[i] = inventory[i] - j
    else:
      print(f"The {i} is not available in {j} quantity")

print(inventory)
