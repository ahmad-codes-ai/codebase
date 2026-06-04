''' Problem 19: Write a program that takes a number from the user and checks if it is a Palindrome (A number that reads the same backward as forward,
like 121 or 5445).  '''

n = int(input("Enter a number: "))
n1 = n
m = ''
while n!=0:
  s = n%10
  s = str(s)
  m+=s
  n = n//10

if str(n1) == m:
  print("Palindrome")
else:
  print("Not palindrome")
