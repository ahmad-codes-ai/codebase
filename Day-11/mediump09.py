'''
### 9. The Server Metrics Rolling Average Alert

A dev monitoring script logs CPU usage percentages every minute in a list. Write a loop that uses a sliding index slice to inspect chunks of 5 consecutive values at a time, calculates their mathematical average, and triggers an alert if any 5-minute chunk average crosses 90%.
'''

l = [85, 87, 92, 88, 91, 93, 89]
idx = 0

for i in range(0,len(l)):
  m = l[idx:idx+5:1]
  if len(m) == 5:
    sum = 0
    for i in m:
      sum+=i
    avg = sum / 5
    if avg > 90:
      print(f"Alert The elements in between the index {idx} and {idx+5} has an average of more than 90%: {avg}%")
  idx+=1
