# Problem 18
# The Database ID Padder
# 
# Systems require integer IDs to be formatted cleanly as strings with leading zeros for consistency. Take a list of raw integer IDs (like 5, 23, 104), and convert them into strings that are exactly 5 characters long, filled with leading zeros.
# 
# **Sample Input:** `[7, 89]`
# 
# **Sample Output:** `["00007", "00089"]`


l = [7,89,5,23,104]
nl = []
for i in l:
  i = str(i)
  l = len(i)
  if l<5:
    m = 5 - l
    i = ('0'*m) + i
    nl.append(i)
  else:
    nl.append(i)

print(nl)

