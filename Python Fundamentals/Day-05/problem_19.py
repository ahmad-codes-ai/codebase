# Problem 19: Case Mod Counter
# Loop through a string and count how many lowercase characters exist versus how many
# uppercase characters exist using string validation methods.

s = input("Enter a string: ")
lo = 0
up = 0

for i in s :
  if i.islower():
    lo+=1
  else:
    up+=1

print(f"Lowercase: {lo}")
print(f"Uppercase: {up}")
