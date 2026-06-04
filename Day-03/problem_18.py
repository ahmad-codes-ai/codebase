''' Problem 18: Take a number from the user. Count how many times the digit 7 appears
 inside that number using math operations. (e.g., Input: 70747, Output: 3).'''

n = int(input("Enter a number: "))
count = 0

while n!=0:
  m = n%10
  n = n//10
  if m == 7:
    count+=1
  else:
    pass

print(f"The digit 7 appears {count} time in this number")
