"""
### 39. The Absolute Difference Array Builder

You have a list of integers. Write a loop to create a new list where each element is the absolute mathematical difference between the original number and the number next to it in the sequence.
"""

l = [4, 10, 15, 8, 12]
nl = []
for i in range(0,len(l) - 1):
  m = l[i] - l[i+1]
  if m < 0:
    m = -m
  nl.append(m)

print(nl)
