"""
### 28. The Dictionary Inverse Value-List Grouping

Take a dictionary where multiple keys share identical string values: {"A": "Admin", "B": "User", "C": "Admin"}. Write a loop structure that flips it into a dictionary where the roles are keys and the values are a list of matching user keys.

**Sample Input:** `{"A": "Admin", "B": "User", "C": "Admin"}`

**Sample Output:** `{"Admin": ["A", "C"], "User": ["B"]}`
"""

d = {"A": "Admin", "B": "User", "C": "Admin"}

final = {}

for k,v in d.items():
  if v not in final:
    final[v] = [k]
  else:
    final[v].append(k)

print(final)
