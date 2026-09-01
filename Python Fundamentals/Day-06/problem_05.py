# Problem: Take a large integer input. Use a while loop to break the number down digit by digit, calculate the sum of all its digits, and print the total.

n = int(input("Enter a large integer: "))
sum = 0

while n!=0:
  m = n%10
  n = n//10
  sum+=m

print(sum)
