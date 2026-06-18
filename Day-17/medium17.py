"""
Problem 17: The E-Commerce Product Variant Matrix
A clothing storefront tracks inventory using item variants. You are given a dictionary where keys are product types and values are tuples of sizes: {"Shirt": ("S", "M", "L")}. Generate a flat inventory list containing dictionaries representing every possible item-size configuration combination.
"""

s = {"Hat": ("S", "M")}
l = []
for k,v in s.items():
  for i in v:
    d = {}
    d['type'] = k
    d['size'] = i
    l.append(d)

print(l)
