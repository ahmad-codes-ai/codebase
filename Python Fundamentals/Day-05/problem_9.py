# Problem 9: Skip-Five Summation
# Use a loop to iterate from 1 to 30. Calculate the total sum of these numbers,
# but use a continue statement to skip any numbers that are perfectly divisible by 5.

sum = 0

for i in range(1,31):
  if i%5 == 0:
    continue
  else:
    sum+=i

print(sum)
