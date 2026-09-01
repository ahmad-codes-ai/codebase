# Problem 27: The Multiplication Block
# Use nested loops to print a small multiplication grid from 1×1 up to 3×3 cleanly.

for i in range(1,4):
  for j in range(1,4):
    m = i*j
    print(f"{i} x {j} = {m}")
