# Problem 22: ASCII Peak Finder
# Take a string input. Loop through it to find and print the single character that
# holds the highest ASCII/Unicode value.

s = input("Enter a string: ")

big = ''

for i in s:
  if i > big:
    big = i
  else:
    pass

print(big)
