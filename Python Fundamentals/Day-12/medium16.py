"""
Problem 16: The Beta Tester Enrollment Validator
A signup sequence collects lists of invitees from multiple sheets. Merge three separate lists of emails into one collection using operations that enforce unique values, then run a loop to strip out any email string that does not contain a valid ".com" extension.
"""

unique_l = []

for i in l1:
  if i.lower() not in unique_l:
    unique_l.append(i)

for j in l2:
  if j.lower() not in unique_l:
    unique_l.append(j)

for k in l3:
  if k.lower() not in unique_l:
    unique_l.append(k)

for i in unique_l:
  if i.endswith('.com'):
    print(i)
