# Problem 24: Manual Substring Search
# Scan a main string for a specific 2-character target (like "ch"). Use a loop to print
# the starting index every time the pattern is found without using .find().

s = input("Enter main string: ")
t = input("Enter target substring")
idx = 0

for i in range(len(s)-1):
  ns = s[i:i+2]
  if ns == t:
    print(f"Found at idx: {idx}")
  idx+=1
