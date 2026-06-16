"""
### 2. The API JSON-Payload Flattener

An LLM API returns user meta-data as a dictionary containing nested lists. Write a script that loops through the dictionary keys, extracts the nested list items, cleanses any trailing whitespaces from them, and saves them into a single, flat global list of elements.
"""

data = {
    "users": ["alice ", "bob  ", "charlie"],
    "metadata": ["active", "inactive  ", "pending"],
    "nested": [["hello  ", "world"], ["foo ", "bar  "]]
}

l = []

for (k,v) in data.items():
  for i in v:
    if type(i) == str:
      i = i.strip()
      l.append(i)
    else:
      for j in i:
        j = j.strip()
        l.append(j)

print(l)
