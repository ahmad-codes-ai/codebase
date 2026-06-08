# Problem: Generate and print the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8\dots$) using a loop. Stop generating as soon as the numbers exceed a maximum limit value input by the user.

n = int(input("Enter max limit: "))

a = 0
b = 1

while True:
  if a>= n:
    break
  else:
    print(a,end=' ')
    sum = a + b
    a = b
    b = sum
