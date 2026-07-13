"""
Problem 23: The Fibonacci Sequence Generator Matrix
Write a program that takes an integer variable n representing a length limit. Use a loop to generate the classic Fibonacci sequence up to that length, storing the results in a list, but filter out all odd values so only the even terms remain.
"""

n = 8
a = 0
b = 1
l = []
final = []
for i in range(n):
  l.append(a)
  c = a + b
  a = b
  b = c

for i in l:
  if i%2 == 0:
    final.append(i)

print(final)
