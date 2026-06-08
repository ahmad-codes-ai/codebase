# Problem: Loop through numbers 1 to 50. Maintain a running total sum of these numbers, but use a continue statement to completely skip any number that is a multiple of both 3 and 5.

sum = 0

for i in range(1,51):
  if i%3 == 0 and i%5 == 0:
    continue
  else:
    sum+=i

print(sum)
