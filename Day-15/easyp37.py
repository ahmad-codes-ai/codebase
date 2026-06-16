"""
### 37. The Dynamic Step Multiplier Loop

Write a program that uses a loop to iterate through numbers from 1 to 30. If the number is a multiple of 3, print its square value. For all other numbers, print the number as it is.
"""

for i in range(1,31):
  if i % 3 == 0:
    print(i**2)
  else:
    print(i)
