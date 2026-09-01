"""
### 47. The Matrix Diagonal Extraction Sprint

You have a nested list representing a square matrix (a list containing three lists of three numbers each). Use explicit index positions inside a loop to find and print the numbers that form the top-left to bottom-right diagonal line.

**Sample Input:** [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

**Sample Output:** Diagonal Elements: 1, 5, 9
"""

l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
nl = []
i = 0

while i<3:
  nl.append(l[i][i])
  i+=1

print(nl)
