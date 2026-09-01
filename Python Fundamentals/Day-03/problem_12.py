# Problem 12: Write a program that calculates the sum of this specific series up to N terms: 1 + 4 + 9 + 16 + ... + N^2 (The sum of squares).

n = int(input("Enter value of n: "))

for i in range(1,n+1):
  print(i*i,end=' ')
