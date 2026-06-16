"""
### 43. The Unique Element Counter (No Sets)

Take a list filled with duplicate integers. Without using Python sets, write a loop that processes the elements one by one and populates a new list only if the element does not already exist inside it.
"""

l = [1, 2, 2, 3, 4, 4, 5, 1, 6]
nl = []

for i in l:
  if i not in nl:
    nl.append(i)

print(nl)
