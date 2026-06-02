"""
Task: Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
"""

n = int(input("Enter value of n: "))

sum = (n * (n + 1) * ((2 * n) + 1)) / 6

print(f"The sum of square of first {n} natural number is : {sum}")
