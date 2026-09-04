'''
Problem 7: Product Filter 🛍️
You have a file called products.json with this content:

json
[
  {"id": 1, "name": "Laptop", "price": 999, "category": "Electronics"},
  {"id": 2, "name": "Chair", "price": 80, "category": "Furniture"},
  {"id": 3, "name": "Headphones", "price": 150, "category": "Electronics"},
  {"id": 4, "name": "Table", "price": 200, "category": "Furniture"},
  {"id": 5, "name": "Mouse", "price": 25, "category": "Electronics"}
]
Your task:

Read products.json.

Filter all products where price > 100.

Save the filtered list to a new file called expensive_products.json with pretty printing (indent=2).
'''

import json

with open('products.json','r') as f:
    data = json.load(f)

filtered_list = []

for item in data:
    if item['price'] > 100:
        filtered_list.append(item)

with open('expensive_products.json','w') as f:
    json.dump(filtered_list,f,indent=2)