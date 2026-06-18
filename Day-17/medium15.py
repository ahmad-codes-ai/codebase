"""
Problem 15: The Git Commit Log Author Classifier
A raw git log dumps strings like "commit:102 | author:ahmad | files:3". Loop through a list of these entries, parse out the author name using string slicing or splitting, and update a dictionary that records how many commits each specific developer has submitted.
"""

d = {}

for i in commit_logs:
  author = i.split('|')[1]
  name = author.split(':')[1]
  name = name.strip()
  if name not in d:
    d[name] = 1
  else:
    d[name]+=1

print(d)
