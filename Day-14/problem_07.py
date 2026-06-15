# Problem 07
# The E-Commerce Cart Totalizer
# 
# A shopping cart is represented as a list of numbers representing item costs. Loop through the list to calculate the total bill, but if the total exceeds 100, apply a flat 10% mathematical discount using arithmetic operators.
# 
# **Sample Input:** `[50, 30, 40]`
# 
# **Sample Output:** `Final Bill: 108.0`


cart = [50, 30, 40]
total = 0

for i in cart:
  total+=i

if total > 100:
  total = total * 0.90

print(f"Final Bill: {total}")

