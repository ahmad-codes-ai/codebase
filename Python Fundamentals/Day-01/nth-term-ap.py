"""
Task: Given the first 2 terms of an Arithmetic Series. Find the Nth term of the series. Assume all inputs are provided by the user.
"""

a1 = int(input("Enter first term: "))
a2 = int(input("Enter second term: "))
n = int(input("Enter value of n: "))

am = a1 + (n - 1) * (a2 - a1)

print(am)
