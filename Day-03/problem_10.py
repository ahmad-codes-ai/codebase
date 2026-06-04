# Problem 10: Ask the user to input a number. If it's positive, print its countdown to 0. If it's negative or zero, print "Invalid"

n = int(input("Enter a number: "))

if n > 0:
  for i in range(n,-1,-1):
    print(i,end=' ')
else:
  print("Invalid")
