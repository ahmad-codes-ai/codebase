# Problem: Track a running count outside and inside a nested loop printing text
count = 0

for i in range(1,5):
  print(count)
  count+=1
  for j in range(1,4):
    print("hello")
