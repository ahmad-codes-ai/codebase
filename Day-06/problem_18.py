# Problem: A raw string contains comma-separated fields: "Ahmad,16,Lahore,ICS". Use string splitting and a loop to print each item cleanly on its own line with a generic item counter prefix (e.g., Field 1: Ahmad).

s = "Ahmad,16,Lahore,ICS"
j = 1

for i in s:
  m = s.split(',')

for i in m:
  print(f"Filed {j}: {i}")
  j+=1
