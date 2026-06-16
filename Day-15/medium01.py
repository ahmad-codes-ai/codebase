"""
### 1. The Multi-Agent Session Heartbeat Aggregator

In Agentic AI, worker nodes report back constantly. You have a list of tuples containing (agent_name, status_code, response_time). Loop through this list, check if the status_code is 200, and if so, append the response_time to a tracking list for that specific agent.

**Sample Input:** [("Scraper", 200, 0.45), ("Writer", 500, 0.0), ("Scraper", 200, 0.38)]

**Sample Output:** scraper_times = [0.45, 0.38]
"""

l =  [("Scraper", 200, 0.45), ("Writer", 500, 0.0), ("Scraper", 200, 0.38)]
d = {}

for name,status,time in l:
  if status == 200:
    if name not in d:
      d[name] = [time]
    else:
      d[name].append(time)

print(d)
