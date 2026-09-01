'''
### 13. The AI Transcript Keyword Extractor

An audio transcription output needs processing. Convert a long text string into a list of words; filter out common filler words (stored in a validation Set like {"um", "ah", "like"}), and create a dictionary mapping the remaining unique words to their frequency count.
'''

text = "um so like I think we should um you know like start the project ah tomorrow"
filler = {"um", "ah", "like", "you", "know"}
lw = text.split()
d = {}

for i in lw:
  if i not in filler:
    if i not in d:
      d[i] = 1
    else:
      d[i]+=1

print(d)
