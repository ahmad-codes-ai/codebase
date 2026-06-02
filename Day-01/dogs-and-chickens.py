"""
Task: Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.
For example: Input: heads -> 4 legs -> 12
Output: dogs -> 2 chicken -> 2
"""

heads = int(input("Enter total heads: "))
legs = int(input("Enter total legs: "))

d = (legs - 2 * heads) // 2
c = heads - d

print(f"Dogs : {d}")
print(f"Chickens : {c}")
