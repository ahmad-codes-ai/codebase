# Problem 9: Take a number N from the user. Print all the numbers from 1 to N but skip any number that is a multiple of 4.

n = int(input("Enter a number: "))

for i in range(1,n+1):
  if i%4 == 0:
    pass
  else:
    print(i,end=' ')
