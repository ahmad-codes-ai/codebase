'''
### 11. The Multi-Agent Task Pipeline Router

An AI pipeline routes jobs based on file extensions. Take a list of file path strings; parse the file extension from the end of each string using slicing, look up which agent processes that extension using a mapping dictionary, and append the filename to that agent's active queue list.
'''

file_paths = [
    "/home/user/data.csv",
    "/docs/report.pdf",
    "/images/photo.jpg",
    "/temp/script.py",
    "/downloads/info.pdf",
    "/photos/background.jpg"
]

agent_mapping = {
    "csv": "DataAgent",
    "pdf": "DocAgent",
    "jpg": "ImageAgent",
    "py": "CodeAgent"
}

d = {}

ext = []
name = []
for i in file_paths:
  l = i.split('.')
  ext.append(l[1])
  m = l[0].split('/')
  m = m[-1]
  name.append(m)



mix = list(zip(name,ext))

for i in range(len(mix)):
  extt = mix[i][-1]        # csv
  nme = mix[i][0]          # data
  nn = agent_mapping[extt]   # Data agent
  if nn not in d:
    d[nn] = [nme+'.'+extt]
  else:
    d[nn].append(nme+'.'+extt)

print(d)
