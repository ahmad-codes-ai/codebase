# Problem 25
# The Terminal Log Timeline Inverter
# 
# Systems append new entries to the bottom of text logs, but a engineer wants to read the freshest updates first. Take a list of log entries and use index slicing mechanics to completely invert the list sequence without using built-in methods.


logs = [
    "2025-01-01 10:00:01 - System started",
    "2025-01-01 10:05:23 - User login: alice",
    "2025-01-01 10:12:47 - File saved: report.pdf",
    "2025-01-01 10:34:12 - User logout: alice",
    "2025-01-01 11:00:05 - System backup initiated",
    "2025-01-01 11:15:33 - Email sent: weekly report",
    "2025-01-01 11:45:20 - Error: disk space low",
    "2025-01-01 12:00:00 - System shutdown"
]

up_logs = logs[::-1]
for i in up_logs:
  print(i)

