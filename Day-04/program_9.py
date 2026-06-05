# Problem: Find and print numbers between 1000 and 3000 where every single digit is even
for i in range(1000,3001):
  m = ''
  s = str(i)
  for n in s:
    n = int(n)
    if n%2 == 0:
      m = m + str(n)
    else:
      pass
  if m == str(i):
    print(i,end=' ')
  else:
    pass
