"""
### 11. System Feature: Database NoSQL Relational Schema Migrator

**Context:** Legacy storage dumps store raw account profiles as unstructured, flat arrays of strings. To support a new application backend, a database transformation module must read these sequential data rows, convert the flat arrays into an optimized relational map structured by individual IDs, and ensure numbers are cast into explicit native data types.

**Input State:**
```python
legacy_rows = [["USR01", "Ahmad", "16"], ["USR02", "Ali", "22"]]
```

**Expected Output State:**
```python
migrated_db = {
    "USR01": {"name": "Ahmad", "age": 16},
    "USR02": {"name": "Ali", "age": 22}
}
```
"""

legacy_rows = [["USR01", "Ahmad", "16"], ["USR02", "Ali", "22"]]
mig_db = {}

for i in legacy_rows:
  d = {'name': i[1] , 'age': int(i[2])}
  mig_db[i[0]] = d

print(mig_db)
