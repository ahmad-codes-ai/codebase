# Problem: Use nested loops to print a downward-facing right-angled triangle of stars based on a user input rows $N$. For $N=4$: * * * * \n * * * \n * * \n *

n = int(input("Enter value of n: "))

for i in range(n,0,-1):
  for j in range(1,i+1):
    print("*",end=' ')
  print()
