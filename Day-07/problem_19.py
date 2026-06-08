# Problem: Take a string input. Loop through it and construct a new string where every even-indexed character is forced to uppercase, and every odd-indexed character is forced to lowercase.

s = input("Enter a string: ")
ls = len(s)

ns = ''

for i in range(0,ls):
  if i%2 == 0:
    m = s[i].upper()
    ns+=m
  else:
    m = s[i].lower()
    ns+=m

print(ns)
