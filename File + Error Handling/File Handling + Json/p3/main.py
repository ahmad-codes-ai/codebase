word = 'quick'


with open('story.txt','r') as f:
   data = f.read()
   final = data.replace(word,'slow')
   print(type(f))

with open('story_modified.txt','w') as f:
   f.write(final)


      
