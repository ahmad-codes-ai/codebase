# Problem 11
# The Command Line Argument Sanitizer
# 
# A CLI tool takes user flags as a string separated by dashes. Convert the raw string into a clean Python list using string splitting, loop through the flags, and remove any flag that is less than 2 characters long.


s = input("Enter your raw string: ")

l = [i for i in s.split()]
ls = []

for i in l:
  if len(i) < 2:
    ls.append(i)
  else:
    pass

for i in ls:
  if i in l:
    l.remove(i)
  else:
    pass

print(l)

