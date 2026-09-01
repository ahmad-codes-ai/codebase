#Problem 4: Take an integer N from the user. Calculate and print the sum of all odd numbers from 1 to N

n = int(input("Enter a number: "))
sum = 0

for i in range(1,n+1,1):
  if i%2 == 0:
    pass
  else:
    sum = sum + i

print(sum)
