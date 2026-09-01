"""
### 26. The Consecutive Element Product Filter

Given a list of integers, loop through the elements up to the second-to-last item. Calculate the mathematical product of the current number multiplied by the next number in line. Append this product to a new tracking list only if the product is divisible by 4.
"""

l = [3, 8, 2, 5, 12, 4, 7, 6, 10, 9]

final = []

for i in range(len(l)-1):
  current = l[i]
  next = l[i+1]
  m = current * next

  if m%4 == 0:
    final.append(m)

print(final)
