''' Problem 13: Take a number from the user.Print all of its mathematical factors (Numbers that divide it completely with a remainder of 0.
 For example, factors of 6 are 1, 2, 3, 6).'''

n = int(input("Enter a number: "))

for i in range(1,n+1):
  if n%i == 0:
    print(i,end=' ')
  else:
    pass
