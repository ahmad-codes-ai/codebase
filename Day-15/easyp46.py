"""
### 46. The Dictionary Key-Value Swapper

Take a basic dictionary containing unique keys and unique values. Write a loop that builds a brand new dictionary where the original values become the keys, and the original keys become the values.

**Sample Input:** {"A": 1, "B": 2}

**Sample Output:** {1: "A", 2: "B"}
"""

d = {"A": 1, "B": 2 , "C" : 3}
nd = {}

for (k,v) in d.items():
  nd[v] = k

print(nd)
