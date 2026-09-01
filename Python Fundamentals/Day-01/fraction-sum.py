"""
Task: Given 2 fractions, find the sum of those 2 fractions. Take the numerator and denominator values of the fractions from the user.
"""

n1 = int(input("Enter numerator of first faraction:  "))
d1 = int(input("Enter denominator of first faraction: "))

n2 = int(input("Enter numerator of second faraction:  "))
d2 = int(input("Enter denominator of second faraction: "))

sum = ((n1 * d2) + (n2 * d1)) / (d1 * d2)

print(sum)
