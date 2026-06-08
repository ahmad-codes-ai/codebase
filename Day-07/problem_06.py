# Problem: Write a program to calculate the sum of this mathematical sequence up to $N$ terms provided by the user using a loop: 1/1! + 2/2! + 3/3! + ... + N/N!

import math
sum = 0
n = int(input("Enter the value of n: "))

for i in range(1,n+1):
  sum = sum + (i/math.factorial(i))

print(sum)
