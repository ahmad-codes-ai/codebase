'''
Problem 1: Log File Analyzer 📊
You have a file called server.log with these contents:

text
INFO User login successful
ERROR Database connection failed
WARNING Disk space low
INFO File uploaded
ERROR Timeout occurred
INFO User logout
WARNING High memory usage
INFO System ready
Your task:

Read server.log.

Count how many lines start with INFO, ERROR, and WARNING.

Write the counts into a new file called log_summary.txt in this format:

text
INFO: 4
ERROR: 2
WARNING: 2
'''

d = {
    'INFO' : 0,
    'ERROR': 0,
    'WARNING': 0,
}

with open('server.log','r') as f:
  while True:
    line = f.readline()
    if line == '':
      break
    d[line.split()[0]]+=1

with open('log_summary.txt','w') as f:
  f.write(f"INFO: {d['INFO']}\nERROR: {d['ERROR']}\nWARNING: {d['WARNING']}")


