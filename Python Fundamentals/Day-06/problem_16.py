# Problem: Take two strings from the user. Use the `sorted()` function on both. Compare the results using relational operators to check if they contain the exact same characters, and print a clean confirmation message.

s1 = sorted(input("Enter string no1: "))
s2 = sorted(input("Enter string no2: "))

if s1 == s2:
  print("Yes")
else:
  print("NO#")
