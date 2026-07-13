# Problem: Use nested loops to print a triangle pattern where each row contains ascending numbers matching the row index. For input $N=4$: 1 \n 1 2 \n 1 2 3 \n 1 2 3 4

n = int(input("Enter value of n: "))

for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end=' ')
  print()
