"""
### 48. The List Element Element-Product Tracker

Given a list of float values, write a loop that creates a matching list where each element at index i is the product of the original number multiplied by its own index integer value (list[i] * i).
"""

l = [0,6,4,2,6]
nl = []
idx = 0
for i in l:
  m = i * idx
  nl.append(m)
  idx+=1

print(nl)
