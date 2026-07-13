# Problem: Take a multi-digit integer as input (e.g., 1234). Using a while loop and mathematical operators (% and //), reverse the integer completely without converting it to a string.

n = int(input("Enter a number: "))
m = 0
while n!=0:
  m = (m*10) + (n%10)
  n = n//10

print(m)
