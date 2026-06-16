"""
### 44. The Two-Dimensional Coordinate Flattener

You have a list containing tuples representing grid coordinates [(1, 2), (3, 4), (5, 6)]. Write a nested loop configuration that extracts every individual integer from those tuples and drops them sequentially into a flat single list.

**Sample Input:** [(1, 2), (3, 4)]

**Sample Output:** [1, 2, 3, 4]
"""

l = [(1, 2), (3, 4), (5, 6)]
nl = []
for i in l:
  for j in i:
    nl.append(j)

print(nl)
