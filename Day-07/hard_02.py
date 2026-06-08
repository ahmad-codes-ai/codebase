# Problem: Take a text paragraph as input. Loop through the words to find the single longest word. Print both the word and its length. If there is a tie, return the word that appears first alphabetically. Do not use built-in sorting methods on the list.

s = input("Enter a text paragraph: ")
l = 0
m = s.split(' ')

for i in m:
  if len(i) > l:
    l = len(i)
    word = i
  elif len(i) == l:
    if i < word:
      word = i
    else:
      pass
  else:
    pass

print(f"The longest word is {word} with {l} characters")
