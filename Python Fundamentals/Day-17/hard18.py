"""
### 18. Core Logic: Recursive-Style Hierarchical Key-Value Flattener

**Context:** Config files exported from legacy cloud infrastructure contain messy, deeply nested parameter trees. To make searching faster, a flattening loop must traverse the dictionary nodes without using recursive function definitions, merge string names using underscore delimiters, and return a clean, un-nested dictionary.

**Input State:**
```python
nested_configuration = {"meta": {"status": "active", "code": 200}, "id": 105}
```

**Expected Output State:**
```python
flat_configuration = {"meta_status": "active", "meta_code": 200, "id": 105}
```
"""

nested_configuration = {"meta": {"status": "active", "code": 200}, "id": 105}
flat_configuration = {}

for i in nested_configuration:
   m = nested_configuration[i]
   if type(m) == dict:
    for k,v in m.items():
      key = i + '_' + k
      val = v
      flat_configuration[key] = val
   else:
     flat_configuration[i] = nested_configuration[i]

print(flat_configuration)
