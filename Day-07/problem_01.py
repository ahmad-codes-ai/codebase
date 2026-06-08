# Problem: Take an integer input greater than 1. Use a for loop to check if it's a prime number. Use Python's unique loop-else structure to print "The number is prime" only if the loop finishes completely without hitting a break.

n = int(input("Enter an integer greater then 1: "))
div = 0

for i in range(1,n+1,1):
  if n%i == 0:
    div+=1
  if div >=3:
    print("Not prime")
    break

else:
  print("Prime")
