''' Problem 14: Ask the user for a number N. Calculate the sum of all numbers from 1 to N,
 but if a number is a multiple of either 3 OR 7, skip it. '''

n = int(input("Enter a number: "))
sum = 0

for i in range(1,n+1):
  if i%3 == 0 or i%7 == 0:
    pass
  else:
    sum+=i

print(sum)
