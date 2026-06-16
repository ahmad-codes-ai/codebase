"""
### 41. The Vowel and Consonant Ratio Counter

Given a lowercase string word, loop through its characters to count the total number of vowels (a, e, i, o, u) and consonants. Print both counts in a final summary statement.
"""

s = input("Enter your string: ").lower().strip()
v = 0
c = 0
vowel = ['a','e','i','o','u']

for i in s:
  if i in vowel:
    v+=1
  else:
    c+=1

print(f"Vowels : {v} \n Consonants : {c}")
