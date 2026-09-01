"""
### 50. The Multi-Type List Splitter

You are given a single Python list containing a mix of string data and integer data. Write a loop that checks the type of each element, splitting them up so all integers land in a list called int_vault and all strings land in a list called str_vault.
"""

l = [10, "apple", 25, "banana", 7, "cherry"]
iv = []
sv = []

for i in l:
  if type(i) == int:
    iv.append(i)
  else:
    sv.append(i)

print(f"Int Vault : {iv} \n Str Vault : {sv}")
