"""
### 4. Incident Report: Multi-Agent Microservice Network Telemetry Analyzer

Context: An edge node router is failing silently. The central dashboard requires a monitoring module that parses sequential telemetry health heartbeats. If the state machine records three consecutive operational failures ("TIMEOUT" or "ERROR") inside a sliding timeline slice, it must immediately halt processing and throw a high-severity critical infrastructure exception log displaying the start index.

Input State:
stream = ["SUCCESS", "TIMEOUT", "ERROR", "ERROR", "SUCCESS", "TIMEOUT"]

Expected Output State:
CRITICAL CRASH ALERT AT INDEX POSITION: 1
"""

stream = ["SUCCESS", "TIMEOUT", "ERROR", "ERROR", "SUCCESS", "TIMEOUT"]

for i in range(len(stream)-2):
  s = stream[i:i+3]
  if 'SUCCESS' in s :
    pass
  else:
    print(f"Critical crash alert at index: {i}")
    break
