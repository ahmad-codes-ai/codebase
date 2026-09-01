# Problem 26
# The Cloud Storage Cost Estimator
# 
# A cloud server charges different monthly micro-fees per gigabyte depending on the data type. Given a dictionary of data type prices and a list of tuples containing (data_type, size_in_gb), loop through the list to calculate the total billing cost.
# 
# **Sample Input:** `prices = {"video": 2, "text": 1}, storage = [("video", 5), ("text", 10)]`
# 
# **Sample Output:** `Total Cost: 20`


prices = {"video": 2, "text": 1}
storage = [("video", 5), ("text", 10)]
total = 0

vrate = prices['video']
trate = prices['text']

for (k,v) in storage:
  if k == 'video':
    total+= v * vrate
  else:
    total+= v * trate

print(total)

