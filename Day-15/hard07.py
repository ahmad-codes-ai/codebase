"""
### 7. System Feature: Command Line Argument Pipeline Parser

**Context:** Developers are building local automation scripts that pass composite shell flags into Lubuntu terminals. The software entry point must break down continuous string blocks split by execution operators (&&), split the individual instructions from their parameters (=), and organize the text chunks into a nested configuration lookup object.

**Input State:**
```python
cli_input = "init --dir=/src && build --target=prod"
```

**Expected Output State:**
```python
{
    "init": {"dir": "/src"},
    "build": {"target": "prod"}
}
```
"""

cli_input = "init --dir=/src && build --target=prod"

d = {}

c = cli_input.split('&&')

for i in c:
  s = i.split('--')
  ss = s[-1].split('=')
  f = {ss[0] : ss[1]}
  d[s[0].strip()] = f

print(d)
