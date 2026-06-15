# Problem 01
# The Clean-Slate Handle Maker
# 
# Users registering for your app typed their preferred handles with messy spaces and mismatched cases. Loop through the raw submission list, strip all leading/trailing whitespace, convert everything to lowercase, and prefix each with an @ symbol if it isn't already there.


users = ["  Alex  ", "sam_j  ", "  @taylor_99", "JORDAN_DEV", " @Casey_K "]
ns = []

for i in users:
  i = i.lower().strip()

  if i.startswith('@'):
    ns.append(i)
  else:
    ns.append('@' + i)

print(ns)

