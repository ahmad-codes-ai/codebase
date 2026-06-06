# Problem 11: Boundary Harvest
# Take a string input. Print a new string made of its first two characters and its
# last two characters using positive and negative indexing combined.

s = input("Enter a string: ")
f2 = s[:2]
l2 = s[-2:]

new = f2 + l2

print(new)
