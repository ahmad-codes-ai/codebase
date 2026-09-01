"""
### 42. The Continuous Int Consolidation Tracker

Set up a loop that continuously simulates processing sequential numbers starting from 1. Accumulate the sum of these numbers inside a variable, and break out of the loop immediately the moment that running sum exceeds 500.
"""

sum = 0
i = 1
while True:
  sum+=i
  if sum > 500:
    break
  i+=1

print(sum)
