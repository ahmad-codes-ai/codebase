"""
### 49. The Conditional Threshold Element Popper

Take an initial list of numbers. Write a loop that checks each number; if a number is less than 10, append it to a list called low_tier, otherwise append its value multiplied by 100 to a list called high_tier.
"""

l = [4,56,3,21,4,7,6,34,12]
low = []
high = []

for i in l:
  if i < 10:
    low.append(i)
  else:
    high.append(i*100)

print(f"Low: {low} \n High: {high}")
