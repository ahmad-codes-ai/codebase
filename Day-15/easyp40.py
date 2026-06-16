"""
### 40. The Factorial Calculation Loop

Take an integer variable (e.g., n = 5). Using a standard while or for loop, calculate its mathematical factorial (5 × 4 × 3 × 2 × 1) and print the final computed integer product.
"""

n = int(input("Enter number to check its factorial: "))
ans = 1
for i in range(1,n+1):
  ans = ans * i

print(ans)
