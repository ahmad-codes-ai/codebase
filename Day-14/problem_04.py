# Problem 04
# The Dev Environment Disk Space Monitor
# 
# Your Lubuntu system logs folder sizes hourly as integers representing gigabytes. Loop through these values; if any log folder size exceeds a specific threshold (e.g., 15GB), print a loud system warning containing the exact index position of that folder.


sizes = [4, 12, 18, 9, 22, 15, 7, 30]
idx = 0

for i in sizes:
  if i > 15:
    print(f"The Folder has exeed the 15gb threshhold at index {idx}")
  else:
    pass
  idx+=1

