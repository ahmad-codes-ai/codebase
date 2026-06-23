"""
### 9. Incident Report: Chat Agent Context Window Overflow Guard

**Context:** An AI model is running out of available context space, throwing token limit errors. The session manager must evaluate active chat lists by counting token footprints backwards from the most recent transaction. The precise moment the threshold index is reached, the older history payload segments must be pruned via index boundaries, and a core system warning notification object must be appended to the top of the history list.

**Input State:**
```python
max_tokens = 100
history = [
    {"role": "user", "text": "old chat 1", "tokens": 60},
    {"role": "assistant", "text": "old chat 2", "tokens": 50},
    {"role": "user", "text": "new chat 3", "tokens": 40},
    {"role": "assistant", "text": "new chat 4", "tokens": 40}
]
```

**Expected Output State:**
```python
compressed_history = [
    {"role": "system", "text": "SYSTEM_WARNING: Context sliced!"},
    {"role": "user", "text": "new chat 3", "tokens": 40},
    {"role": "assistant", "text": "new chat 4", "tokens": 40}
]
```
"""

max_tokens = 100
history = [
    {"role": "user", "text": "old chat 1", "tokens": 60},
    {"role": "assistant", "text": "old chat 2", "tokens": 50},
    {"role": "user", "text": "new chat 3", "tokens": 40},
    {"role": "assistant", "text": "new chat 4", "tokens": 40}
]


compressed_history = []
r_history = history[::-1]
total = 0

for i in r_history:
  if (total + i['tokens']) <= 100:
    total+= i['tokens']
    compressed_history.append(i)
  else:
    break

compressed_history.reverse()
d = {"role": "system", "text": "SYSTEM_WARNING: Context sliced!"}
compressed_history.insert(0,d)

print(compressed_history)
