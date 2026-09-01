"""
### 1. Nested Billing Report

Write a Python script that loops through the raw logs and generates a structured Nested Billing Report that groups everything by Agent Name, then splits their usage by Model Type, and sums up the total tokens spent.

**Input State:**
```python
raw_logs = [
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 1200},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 3500},
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 800},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 1500},
    {"agent": "Writer_Agent", "model": "llama-3", "tokens": 2200},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 900},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 4000}
]
```

**Expected Output State:**
```python
{
    "Scraper_Agent": {"llama-3": 2000},
    "Writer_Agent": {"gpt-4o": 7500, "llama-3": 2200},
    "Reviewer_Agent": {"gpt-4o": 2400}
}
```
"""

raw_logs = [
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 1200},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 3500},
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 800},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 1500},
    {"agent": "Writer_Agent", "model": "llama-3", "tokens": 2200},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 900},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 4000}
]


d = {}

for i in raw_logs:
  name = i['agent']
  model = i['model']
  tokens = i['tokens']

  if name not in d:
    f = {model : tokens}
    d[name] = f
  else:
    if model not in d[name]:
      d[name][model] = tokens
    else:
      d[name][model]+=tokens

print(d)
