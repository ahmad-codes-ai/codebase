"""
### 27. The Bi-Directional List Peak Hunter

Write a loop that parses an array of numbers to locate "peak" elements. A peak is an element that is strictly greater than both the element immediately preceding it and the element immediately following it in the index order.
"""

l = [2, 5, 3, 8, 1, 6, 4]

peak = []

for i in range(1,len(l)-1):
  prev = l[i-1]
  crr = l[i]
  next = l[i+1]

  if crr > prev and crr > next:
    peak.append(crr)

print(peak)
