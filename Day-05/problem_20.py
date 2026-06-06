# Problem 20: Character Multiplier Loop
# Take a string input. Use a loop to print each character of the string repeated 3 times
# (e.g., "abc" becomes "aaabbbccc").

s = input("Enter a string: ")

for i in s:
  print(i*3,end='')
