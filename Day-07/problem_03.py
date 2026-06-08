# Problem: A 3-digit number is an Armstrong number if the sum of the cubes of its digits equals the number itself (e.g., $153 = 1^3 + 5^3 + 3^3$). Take a 3-digit integer input and verify if it matches this criteria using a math loop.

n = int(input("Enter a 3 digit number: "))
n2 = n
sum = 0

while n!=0:
  m = n%10
  n = n//10
  sum = sum + (m*m*m)

if sum == n2:
  print("Armstrong")
else:
  print("Not Armstrong")
