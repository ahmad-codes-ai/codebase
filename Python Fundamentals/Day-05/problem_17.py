# Problem 17: Manual Space Replacer
# Loop through a sentence entered by a user. Build a brand new string character by character
# where every space (" ") is replaced by an underscore (_).

s = input("Enter a sentence: ")
ns = ''
for i in s:
  if i == ' ':
    i = '_'
  ns+=i

print(ns)
