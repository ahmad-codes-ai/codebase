# Problem 6: Count how many numbers between 1 and 50 are perfectly divisible by 3. Print the final count.

count = 0

for i in range(1,51):
  if i%3 == 0:
    count+=1
  else:
    pass

print(count)
