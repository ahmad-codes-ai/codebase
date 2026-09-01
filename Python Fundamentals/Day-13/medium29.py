"""
### 29. The Mathematical Prime Number Finder Sieve

Given an integer upper bound variable (e.g., limit = 50), write a nested loop system that evaluates every number from 2 up to that limit, uses mathematical conditional division to determine if the number is prime, and appends all prime instances to a clean list.
"""

n = int(input("Enter value of n: "))
l = []
is_prime = True
for i in range(2,n+1):
  count = 0
  for j in range(1,i+1):
    if i%j == 0:
      count+=1
  if count > 2:
    is_prime = False
  else:
    is_prime = True

  if is_prime:
    l.append(i)

print(l)
