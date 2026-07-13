# Problem 23
# The AI Output Length Normalizer
# 
# An LLM generates variable sentence lengths, but your UI grid only supports short blurbs. Take a list of generated strings; if a string's length is greater than 30 characters, use slicing to crop it down to 27 characters and append "..." to the end.


s = input("Enter your sentence: ")

l = len(s)

if l <= 30:
  print(s)
else:
  print(s[0:28] + '...')

