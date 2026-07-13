# Problem 31
# The CSV Data Row Counter
# 
# A backend script reads a mock comma-separated line of data as a single string. Count how many commas exist in that string using a loop or string count method, and add 1 to figure out the total number of distinct data columns in that row.


# Method 1:
s = "Apple,Banana,Orange,Grapes"

l = s.split(',')
col = len(l)

print(f"There are total {col} columns in this string")

# Method 2:
s = "Apple,Banana,Orange,Grapes"
count = 0
for i in s:
  if i == ',':
    count+=1

col = count + 1
print(f"There are total {col} columns in this string")

