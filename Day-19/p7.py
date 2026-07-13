"""
### PROBLEM 7: Logger System
Create a function `log_event()` that:

* Takes required `level` (like "INFO", "ERROR")
* Takes any number of `*messages`
* Takes optional `uppercase` defaulting to False
* Prints formatted log messages
"""

def log_event(level,*messages,upper=False):
  if upper:
    print(level.upper(),':',end=' ')
    for i in messages:
      print(i.upper(),end='-')
  else:
    print(level,':',end=' ')
    for i in messages:
      print(i,end='-')
log_event('Error','system failed','server crashed')
