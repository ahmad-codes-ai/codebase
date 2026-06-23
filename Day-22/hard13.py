"""
### 13. System Feature: Automated Server Linux Storage Cleaner Log

**Context:** Production server drives are filling up, degrading application speeds. An automation script sweeps disk directory nodes. The cleaner module must read file paths, storage footprints, and inactivity counters; identify files residing inside temporary paths ("/tmp/") with an inactivity status greater than 30 loops, remove them from the active index tracking list, and increment a storage bytes reclaimed tracking counter.

**Input State:**
```python
system_files = [
    {"path": "/src/main.py", "size": 500, "unused_days": 40},
    {"path": "/tmp/cache.txt", "size": 1200, "unused_days": 35}
]
```

**Expected Output State:**
```python
cleaned_files = [{"path": "/src/main.py", "size": 500, "unused_days": 40}]
bytes_reclaimed = 1200
```
"""

system_files = [
    {"path": "/src/main.py", "size": 500, "unused_days": 40},
    {"path": "/tmp/cache.txt", "size": 1200, "unused_days": 35}
]

cleaned_files = []
bytes_reclaimed = 0


for i in system_files:
  path = i['path']
  unuse = i['unused_days']

  if path.startswith('/tmp') and unuse > 30:
    bytes_reclaimed += i['size']
  else:
    cleaned_files.append(i)

print(cleaned_files)
print(bytes_reclaimed)
