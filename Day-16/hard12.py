"""
### 12. System Feature: Version Control Blame Log Analytics Engine

**Context:** Project leads want to analyze git repository velocity. The source parsing system outputs data rows mapping files, authors, and specific line modifications. The engine must compile total tracking statistics per engineer, map individual footprints, and leverage set mechanics to isolate which files have been modified by every single active developer on the team roster.

**Input State:**
```python
blame_logs = [("main.py", "ahmad", 10), ("main.py", "ali", 5), ("utils.py", "ahmad", 2)]
```

**Expected Output State:**
```python
author_impact = {"ahmad": 12, "ali": 5}
fully_shared_files = {"main.py"}
```
"""

blame_logs = [("main.py", "ahmad", 10), ("main.py", "ali", 5), ("utils.py", "ahmad", 2)]
author_impact = {}
shared_files = set()
for f,n,l in blame_logs:
  if n not in author_impact:
    author_impact[n] = l
  else:
    author_impact[n]+=l

all_devs = {i for i in author_impact}
all_files = {i[0] for i in blame_logs}

d = {}
for i in all_files:
  d[i] = []

for f,n,l in blame_logs:
  d[f].append(n)


for i in d:
  if set(d[i]) == all_devs:
    shared_files.add(i)

print(author_impact)
print(shared_files)
