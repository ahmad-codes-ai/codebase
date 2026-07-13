# Problem: Use nested loops to generate coordinate pairs $(x, y)$ where $x$ runs from 1 to 4 and $y$ runs from 1 to 4. Add an internal condition that only prints the pair if $x \neq y$ and the product of $x \times y$ is an even number.

for x in range(1,5):
  for y in range(1,5):
    if x!=y and (x*y)%2 == 0:
      print(f"({x},{y})")
    else:
      pass
