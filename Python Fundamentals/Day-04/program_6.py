# Problem: Find and print all prime numbers between a user-defined lower and upper limit
l = int(input("Enter lower limit: "))
u = int(input("Enter upper limit: "))
fact = 0

for i in range(l,u+1,1):
  for j in range(1,i+1,1):
    if (i%j == 0):
      fact+=1
  if fact == 2:
    print(i,end=' ')
  else:
    pass
  fact = 0
