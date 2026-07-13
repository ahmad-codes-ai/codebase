# Problem 13
# The Live Streaming Uptime Ratio Calc
# 
# A streaming bot records system state fractions over a duration. Take a list of integers where 1 represents a stable stream hour and 0 represents a dropped stream. Calculate the total uptime percentage by processing the list with a loop.


l = [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1]
total = len(l)
up = 0
down = 0

for i in l:
  if i == 1:
    up+=1
  else:
    down+=1



print(f"The live stream was stable {(up / total) * 100} percent of time")

