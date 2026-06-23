"""
### 14. System Feature: Multi-Agent Directed Acyclic Graph Dependency Resolver

**Context:** An AI supervisor agent is initiating specialized task pipelines. A dependency verification engine must step through a configuration map detailing which prerequisite features must be running before a worker node can execute. The system must cross-reference active processes, identify which software workflows are blocked due to unfulfilled prerequisites, and output a clean execution queue.

**Input State:**
```python
active_modules = {"db_connected", "config_loaded"}
dependencies = {
    "auth_agent": ["db_connected", "config_loaded"],
    "scraper_agent": ["proxy_initialized"]
}
```

**Expected Output State:**
```python
ready_queue = ["auth_agent"]
blocked_queue = ["scraper_agent"]
```
"""

active_modules = {"db_connected", "config_loaded"}
dependencies = {
    "auth_agent": ["db_connected", "config_loaded"],
    "scraper_agent": ["proxy_initialized"]
}

ready_queue = []
blocked_queue = []

for i in dependencies:
  m = dependencies[i]
  satisfy = True
  for j in m:
    if j not in active_modules:
      satisfy = False
      break
  if satisfy:
    ready_queue.append(i)
  else:
    blocked_queue.append(i)

print(ready_queue)
print(blocked_queue)
