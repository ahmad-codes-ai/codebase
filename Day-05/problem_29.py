# Problem 29: Secure Find Implementation
# Take a paragraph and a target word. Use string searching methods to print the index of the word,
# but explicitly handle it so it returns a clean message instead of throwing an error if the word isn't found.

s = input("Enter a sentence: ")
t = input("Enter target to find: ")
idx = s.find(t)

if idx == -1:
  print(f"{t} does not exist in this sentence")
else:
  print(f"{t} found at index of {idx}")
