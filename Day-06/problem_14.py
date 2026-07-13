# Problem: Take a long sentence input. Without using the built-in `.count()` string method, loop through the string and manually count how many spaces exist to determine the total word count.

s = input("Enter a long sentence: ")
word = 1

for i in s:
  if i == ' ':
    word+=1
  else:
    pass

print(f"There are total {word} words in this sentence")
