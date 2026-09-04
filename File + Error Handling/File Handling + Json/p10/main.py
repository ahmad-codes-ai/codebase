'''
Problem 10: Data Merger (Join Users and Orders) 🔗
You have two files:

users.json:

json
[
  {"user_id": 1, "name": "Alice"},
  {"user_id": 2, "name": "Bob"},
  {"user_id": 3, "name": "Charlie"}
]
orders.json:

json
[
  {"user_id": 1, "product": "Laptop", "amount": 1200},
  {"user_id": 1, "product": "Mouse", "amount": 25},
  {"user_id": 2, "product": "Keyboard", "amount": 75},
  {"user_id": 3, "product": "Monitor", "amount": 300}
]
Your task:

Read both files.

Create a merged structure that looks like this:

json
[
  {
    "name": "Alice",
    "orders": [
      {"product": "Laptop", "amount": 1200},
      {"product": "Mouse", "amount": 25}
    ]
  },
  {
    "name": "Bob",
    "orders": [
      {"product": "Keyboard", "amount": 75}
    ]
  },
  {
    "name": "Charlie",
    "orders": [
      {"product": "Monitor", "amount": 300}
    ]
  }
]
Save the merged result to user_orders.json with pretty printing.

'''

import json

with open('users.json', 'r') as f:
    users = json.load(f)

with open('orders.json', 'r') as o:
    orders = json.load(o)

merged = []

for user in users:
    user_orders = []
    
    for order in orders:
        if order['user_id'] == user['user_id']:
            user_orders.append({
                'product': order['product'],
                'amount': order['amount']
            })
    
    merged.append({
        'name': user['name'],
        'orders': user_orders
    })

print(merged)

