"""
Problem 24: The Sliding Window Sub-String Search
Given a master text string and a fixed length integer k, use a loop and string slicing to find every single distinct substring slice of exactly length k. Store these unique blocks inside a Python Set structure to ensure no repeats.
"""

text = "ABRACADABRA"
k = 3
unique = set()
for i in range(len(text)):
  s = text[i:i+k:1]
  if len(s) == 3:
    unique.add(s)

print(unique)
