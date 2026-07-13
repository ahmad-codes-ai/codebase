# Problem: Take a string input. Without using slicing or `[::-1]`, use a single for loop to manually verify if a string is a palindrome by comparing the character at index i with the character at its matching negative index from the back.

s = input("Enter a string: ")
ls = len(s)
count = 0

for i in range(1,ls+1):
  if s[i-1] == s[-i]:
    count+=1
  else:
    break

if count == ls:
  print("Palindrome")
else:
  print("Not palindrome")
