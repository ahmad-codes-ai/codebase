"""
Task: Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.
"""

p = float(input("Enter principle: "))
r = float(input("Enter intrest: "))
t = float(input("Enter time period: "))

si = (p * r * t) / 100

print(si)
