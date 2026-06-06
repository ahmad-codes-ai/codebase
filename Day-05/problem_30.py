# Problem 30: Random Integer Guessing
# Import the random module. Generate a random target number between 1 and 5.
# Use a while loop to let the user guess until they get it right.

import random

target = random.randint(1,5)
idx = 1

while True:
  user = int(input("Enter a number: "))
  if user == target:
    print(f"You guess correct in {idx} attempts ")
    break
  else:
    print("Wrong guess try again")
  idx+=1
