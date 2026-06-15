# Problem 15
# The AI Transcript Punctuation Stripper
# 
# Raw speech-to-text outputs contain excessive periods and commas that mess up token counts. Take a raw string paragraph, loop through it character by character, and build a new string that completely excludes periods (.) and commas (,).


s = input("Enter a raw string paragraph: ")
ns = ''
for i in s:
  if i == '.' or i == ',':
    pass
  else:
    ns = ns + i

print(ns)

