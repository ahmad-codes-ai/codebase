"""
### 30. The Multi-Type Key-Value Integrity Check

You have a dictionary containing mixed data types as values. Write a loop that inspects each key-value pair; if the value is a string, check if it's numeric and cast it; if it's an empty list, remove the key entirely; and output the finalized clean dictionary state.
"""

d = {
  "name": "John",
  "age": "30",
  "score": "85.5",
  "tags": [],
  "active": True,
  "numbers": [1, 2, 3]
}
final = {}

for k,v in d.items():
  if type(v) == str:
    if v.isalpha() == False:
     if v.isdigit():
       v = int(v)
     else:
      v = float(v)
  elif type(v) == list:
    if len(v) == 0:
      continue
  final[k] = v

print(final)
