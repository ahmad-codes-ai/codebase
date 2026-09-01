'''Problem 15: Write a program that keeps asking the user for a number. Keep a running total. If the user enters a negative number,
 ignore that number (don't add it to the sum) but keep the loop running. Stop only when they enter 0 '''

sum = 0
while True:
  n = int(input("Enter a number: "))
  if n > 0:
    sum+=n
  elif n < 0:
    pass
  else:
    break

print(f"The running total is : {sum}")
