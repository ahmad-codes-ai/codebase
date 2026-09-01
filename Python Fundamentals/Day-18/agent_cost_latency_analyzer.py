"""
### 2. Agent Cost & Latency Analyzer

Write a Python script that loops through execution telemetry logs, calculates the total cost per agent per model using a cost matrix (price per 1,000 tokens), tracks and averages the latency per agent per model, and outputs a nested report grouped by Agent Name then Model Type.

**Input State:**
```python
execution_logs = [
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 1500, "latency": 0.8},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 4000, "latency": 2.1},
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 500, "latency": 0.4},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 2000, "latency": 1.5},
    {"agent": "Writer_Agent", "model": "llama-3", "tokens": 3000, "latency": 1.2},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 1000, "latency": 0.9},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 2000, "latency": 1.8}
]
cost_matrix = {"gpt-4o": 0.015, "llama-3": 0.002}
```

**Expected Output State:**
```python
{
    "Scraper_Agent": {"llama-3": {"total_cost": 0.004, "latency": 0.6}},
    "Writer_Agent": {"gpt-4o": {"total_cost": 0.09, "latency": 1.95}, "llama-3": {"total_cost": 0.006, "latency": 1.2}},
    "Reviewer_Agent": {"gpt-4o": {"total_cost": 0.045, "latency": 1.2}}
}
```
"""

# Raw telemetry log stream
execution_logs = [
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 1500, "latency": 0.8},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 4000, "latency": 2.1},
    {"agent": "Scraper_Agent", "model": "llama-3", "tokens": 500, "latency": 0.4},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 2000, "latency": 1.5},
    {"agent": "Writer_Agent", "model": "llama-3", "tokens": 3000, "latency": 1.2},
    {"agent": "Reviewer_Agent", "model": "gpt-4o", "tokens": 1000, "latency": 0.9},
    {"agent": "Writer_Agent", "model": "gpt-4o", "tokens": 2000, "latency": 1.8}
]

# Price per 1,000 tokens mapping
cost_matrix = {
    "gpt-4o": 0.015,   # $0.015 per 1k tokens
    "llama-3": 0.002   # $0.002 per 1k tokens
}


d = {}

for i in execution_logs:
  agent = i['agent']
  model = i['model']
  tokens = i['tokens']
  lat = i['latency']
  cost = (tokens * cost_matrix[model]) / 1000
  if agent not in d:
    d[agent] = {model : {'total_cost' : cost , 'latency': lat , 'count' : 1}}
  else:
    if model not in d[agent]:
      d[agent][model] = {'total_cost': cost , 'latency' : lat , 'count' : 1}
    else:
      d[agent][model]['total_cost']+= cost
      nl = (d[agent][model]['latency'] + lat)
      d[agent][model]['count']+=1
      d[agent][model]['latency'] = nl


for i in d:
  for j in d[i]:
    d[i][j]['latency'] = round(d[i][j]['latency'] / d[i][j]['count'],2)
    del d[i][j]['count']

print(d)
