"""
### 20. Core Logic: The Production Workflow Pipeline Crucible

**Context:** This is the ultimate integration compiler. The script must ingest a multiline string representing a complete raw production telemetry stream. The application engine must parse the text segments, sanitize whitespace and formatting anomalies, build unique sets of target profiles, map structural associations inside layered dictionaries, handle missing keys or values without throwing runtime fatal exceptions, and print a finalized system audit dashboard.

**Input State:**
```python
payload = "USER:ahmad|TIER:free\nUSER:ali|TIER:pro\nUSER:ahmad|TIER:pro"
```

**Expected Output State:**"""

payload = "USER:ahmad|TIER:free\nUSER:ali|TIER:pro\nUSER:ahmad|TIER:pro"
users = {}
l = payload.split('\n')

for i in l:
  m = i.split('|')
  key = m[0].split(':')[1]
  val = m[1].split(':')[1]
  users[key] = val

unique = len(users)

print("--- CRUCIBLE AGGREGATION METRICS ---")
print(f"Unique Profiles Tracked: {unique}")
print(f"Sanitized Roster State: {users}")
print("------------------------------------")
