# Problem 09
# The Multi-Agent Heartbeat Checker
# 
# An orchestrator checks if worker agents are running using a list of tuples representing (agent_name, status_code). Loop through the tuples; if the status code is 0, print that the agent is healthy, otherwise print that it needs a manual restart.
# 
# **Sample Input:** `[("Scraper", 0), ("Writer", 1)]`
# 
# **Sample Output:** `"Scraper is healthy", "Writer needs a manual restart"`


agents = [("Scraper", 0), ("Writer", 1)]

for (name,health) in agents:
  if health == 0:
    print(f"{name} is healthy")
  else:
    print(f"{name} need a manual restart")

