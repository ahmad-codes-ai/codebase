'''
### 6. The AI Prompt Injection Log Parser

Security firewalls read text outputs from users. Take a long multi-line text string representing system prompts, split it into lines, scan each line for restricted security words stored inside a predefined verification Set, and build a dictionary counting how many malicious terms were caught per line.
'''

text = "User requested data\nSELECT * FROM customers\nNormal operation continued\nDROP TABLE employees\nUPDATE salaries SET amount=50000\nRegular log entry here\nDELETE FROM logs WHERE date<'2025-01-01'\nALTER TABLE users ADD COLUMN age\nSystem running smoothly\nUNION SELECT password FROM admins\nBackup completed successfully\nTRUNCATE TABLE temp_data\nEND OF LOG"

bad_words = {"DROP", "DELETE", "ALTER", "TRUNCATE", "UPDATE", "INSERT", "EXEC", "UNION", "SELECT", "SCRIPT"}
l = text.split('\n')
d = {}
count = 0
line = 1

for i in l:
  m = i.split(' ')
  for j in m:
    if j.upper() in bad_words:
      count+=1
  d[line] = count
  line+=1
  count = 0

print(d)
