# Problem 26: Right-Angled Star Block
# Use nested loops to print a right-angled triangle pattern of stars (*) based on a user input integer N.

n = int(input("Enter value of n: "))

for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end=' ')
  print()
