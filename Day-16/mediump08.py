'''
### 8. The CLI Command Flag Orchestrator

A command-line script takes a user command string like "run --agent=scraper --mode=fast --verbose". Split the string, loop through the elements, extract any element containing an equals sign (=), split it at the delimiter, and populate an active config_panel configuration dictionary.

**Sample Input:** `"start --model=llama3 --tokens=2048"`

**Sample Output:** `{"model": "llama3", "tokens": "2048"}`
'''

user = "start --model=llama3 --tokens=2048"
l = user.split('--')
m = []
d = {}

for i in l:
  if '=' in i:
    m.append(i)

for j in m:
  s = j.split('=')
  d[s[0].strip()] = s[1].strip()

print(d)
