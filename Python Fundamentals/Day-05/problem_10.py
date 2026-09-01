# Problem 10: The Break Tracker
# Iterate through a user-provided string character by character. If the loop encounters
# any uppercase letter, terminate the loop instantly using break and print the index position where it stopped.

user = input("Enter a string: ")
idx = 0

for i in user:
  if i == i.upper():
    print(idx)
    break
  idx+=1
