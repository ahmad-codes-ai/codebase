''' Problem 11: Take 10 separate numbers as input from the user one by one inside a loop.
 At the end, print how many of those 10 numbers were positive and how many were negative.'''

i = 1
pos = 0
neg = 0

while i<=10:
  n = int(input("Enter a positive or negative number: "))
  if n > 0:
    pos+=1
  elif n < 0:
    neg+=1
  else:
    pass
  i+=1

print(f"Positive: {pos}    Negative: {neg}")
