"""
Task: Write a program to find the euclidean distance between two coordinates. Take both the coordinates from the user as input.
"""

x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))

y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(d)
