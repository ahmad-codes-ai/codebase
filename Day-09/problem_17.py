# Problem 17
# The Social Media Hashtag Harvester
# 
# A scraper extracts single post strings. Loop through a list of words extracted from a post; if a word starts with the character "#", append it to a list called active_tags. Otherwise, ignore it.


s = "Just learned about #Python and #AI today! #coding"
l = [i.strip(' " ') for i in s.split()]
active_tags = []

for i in l:
  i = i.strip()
  if i.startswith('#'):
    active_tags.append(i)
  else:
    pass

print(active_tags)

