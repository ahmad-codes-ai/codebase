# Problem 16: Vowel Isolation Loop
# Run a for loop over a user-provided string. Print only the characters that are vowels,
# skipping consonants entirely without creating a new string.

s = input("Enter a string: ")

for i in s:
  i = i.lower()
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    print(i,end=' ')
  else:
    pass
