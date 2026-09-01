"""
Problem 25: The Nested Matrix Transposition Loop
You are given a 3 × 3 matrix represented as a nested list of lists. Write a nested loop configuration that transposes the matrix manually (flipping its rows into columns) and stores the structural result inside a fresh nested list.
"""

l = [[1,2],
     [3,4]]

m = l[0]
n = l[1]

final = list(zip(m,n))

print(final)     # Need Review problem said solve with nested loop but wasn't able to make logic
