"""
### 3. System Feature: E-Commerce Inventory Slicing & Backorder Engine

Context: During a flash sale event, concurrent checkouts cause a massive database race condition. The inventory ledger must process an order pipeline. If an item inventory runs out mid-order, the system must exhaust all remaining physical units, recalculate the user's specific invoice based on partial fulfillment, generate a dynamic delta entry, and route the unfulfilled item quantity to a specialized backorder matrix.

Input State:
inventory = {"Laptop": 2, "Mouse": 5}
orders = {
    "user_alpha": [("Laptop", 1), ("Mouse", 10)],
    "user_beta": [("Laptop", 2)]
}

Expected Output State:
updated_inventory = {"Laptop": 0, "Mouse": 0}
bills = {"user_alpha": 125, "user_beta": 100}  # Assume Base Prices: Laptop=100, Mouse=5
backorder_ledger = {"user_alpha": [("Mouse", 5)], "user_beta": [("Laptop", 1)]}
"""

inventory = {"Laptop": 2, "Mouse": 5}
prices = {'Laptop':100, 'Mouse': 5}

orders = {
    "user_alpha": [("Laptop", 1), ("Mouse", 10)],
    "user_beta": [("Laptop", 2)]
}
bills = {}
back_order = {}

for k,v in orders.items():
  total = 0
  for i,j in v:
    if inventory[i] >= j:
      pass
    else:
      rem = j - inventory[i]
      rem_n = i
      if k not in back_order:
        back_order[k] = [(rem_n,rem)]
      else:
        back_order[k].append((rem_n,rem))
      j = inventory[i]

    inventory[i]-= j
    total += prices[i] * j
    bills[k] = total

print(bills)
print(inventory)

print(back_order)
