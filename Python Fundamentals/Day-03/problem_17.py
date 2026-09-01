'''Problem 17: Take a large integer input from the user (like 4532). Without converting it to a string,
 calculate and print the sum of its individual digits (e.g., 4+5+3+2 = 14).'''

n = int(input("Enter a large number: "))
sum = 0
m = n
while n!=0:
  sum = sum + n%10
  n = n//10

print(f"The sum of individual digits of {m} is {sum}")
