"""
Problem 22: The Manual Selection Sorting Loop
Take an unsorted list of integers. Without using Python's built-in .sort() or sorted(), write a nested loop sequence that manually sorts the numbers in ascending order by repeatedly finding the minimum element and shifting it.
"""

len_l = len(l)
sl = []
for i in range(len_l) :
  min = l[0]
  for j in l:
    if j < min:
      min = j
  sl.append(min)
  l.remove(min)

print(sl)
