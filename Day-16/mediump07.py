'''
### 7. The Network Router Device Blacklist Filter

A Lubuntu-based script monitors active network devices using a list of MAC address strings. Compare this list against a Set of blacklisted addresses; extract all safe addresses into a new list, while converting their format from lowercase to uppercase separated by colons.
'''

active = ["aa:bb:cc:dd:ee:ff", "11:22:33:44:55:66", "ab:cd:ef:12:34:56", "ff:ee:dd:cc:bb:aa"]
blacklist = {"FF:EE:DD:CC:BB:AA", "00:11:22:33:44:55"}
safe = []

for i in active:
  m = i.upper()
  if m not in blacklist:
    safe.append(m)

print(safe)
