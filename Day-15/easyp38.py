"""
### 38. The Alternate Index Slicer Comparison

Take a string input from a variable. Use slicing to separate the characters at odd index positions from the characters at even index positions, and concatenate the two resulting strings together into one final sequence.
"""

s = input("Enter your word: ")
even = s[::2]
odd = s[1::2]
print(even + odd)
