# Problem 8: Write a program that keeps adding numbers from 1, 2, 3... onwards. Stop the loop and print the total sum the exact moment the sum crosses 100.

count = 0
sum = 0

for i in range(1,200):
  if (sum < 100) :
    sum = sum + i
  else:
    break
  count+=1

print(f"The total sum after crossing 100 is {sum} at {count} iteration")
