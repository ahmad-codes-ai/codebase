# Problem: Loop through a string and build a completely new string that retains all original characters except for the vowels. Ensure uppercase and lowercase vowels are both stripped while preserving the casing of consonants.

s = input("Enter a string: ")
ns = ''
for i in s :
  i = i.lower()
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    pass
  else:
    ns+=i

print(ns)
