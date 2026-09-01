# Problem 02
# The CRM Duplicate Evaporator
# 
# A client database has duplicate email entries because of case sensitivity (e.g., Ahmad@email.com and ahmad@email.com). Loop through the list, normalize all strings to lowercase, and use a Python data structure to output a collection where each email appears exactly once.


l = ["Ahmad@email.com", "ahmad@email.com", "Sara.Jones@domain.com", "sara.jones@domain.com", "AHMAD@email.com", "clara_b@tech.org"]
s = set()

for i in l:
  i = i.lower().strip()
  s.add(i)

print(s)

