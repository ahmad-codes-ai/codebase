# Problem 08
# The Text-Bot Word Slicer
# 
# An NLP bot needs to look at the first few characters of incoming phrases. Take a list of sentences, use string index slicing to extract exactly the first 5 characters of each sentence, and append those fragments to a new tracking list.


sentences = [
    "Hello world, how are you?",
    "Python is great for NLP",
    "12345 is the first five digits",
    "Short",
    "     spaced out",
    "HTTP://example.com",
    "!help show me commands",
    "Hello! How can I assist?",
    "Hi there",
    "Hey!"
]

new = []
for i in sentences:
  m = i[0:5]
  new.append(m)

print(new)

