# Problem 2: Take a number N from the user. Print the multiplication table of that number up to 10.

n = int(input("Enter a number: "))

for i in range(1,11):
  m = n * i
  print(f"{n} x {i} = {m}")
