"""
### 36. The Manual Minimum Finder

Take a list of un-ordered integers. Without using Python's built-in min() function, write a loop that iterates through the sequence, keeps track of the smallest number found so far, and prints it at the end.

**Sample Input:** [18, 4, 25, 2, 9]

**Sample Output:** Smallest: 2
"""

p = [18,4,25,2,9]
min = p[0]

for i in p:
  if i < min:
    min = i

print(min)
