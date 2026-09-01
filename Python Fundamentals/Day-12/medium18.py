"""
Problem 18: The Local Host IP Scanner & Logger
An infrastructure monitoring loop tracks network pings. Given a list of status strings like "192.168.1.5:UP", "192.168.1.10:DOWN", loop through the entries, split them at the colon boundary, and store them into a dictionary separated into two sub-lists: "online" and "offline".
"""

d = {'online': [],
     'offline': []}

for i in ip:
  l = i.split(':')[-1]
  if l == 'UP':
    d["online"].append(i.split(':')[0])
  else:
    d["offline"].append(i.split(':')[0])

print(d)
