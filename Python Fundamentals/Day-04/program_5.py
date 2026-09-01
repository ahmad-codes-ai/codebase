# Problem: Print a number pyramid that increases and then decreases in each row
for i in range(1,5):
  for j in range(1,i+1):
    print(j,end='')
  for k in range(j-1,0,-1):
    print(k,end='')
  print()
