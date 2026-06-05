# Problem: Print multiplication tables from 1 to 5, each up to 10
for i in range(1,6):
  for j in range(1,11):
    m = i * j
    print(f"{i} x {j} = {m}")
