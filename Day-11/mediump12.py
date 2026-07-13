'''
### 12. The Database User Profile Normalizer

Legacy user profiles have messy fields: [{"name": " ahmad ", "age": "16 "}]. Loop through this list of dictionaries, clean up all whitespaces, cast numeric strings to actual integers, and output a completely sanitized list of dictionaries.
'''

raw =  [
    {"name": " ahmad ", "age": "16 "},
    {"name": "  sarah ", "age": " 25"},
    {"name": "john ", "age": "30 "}
]


final = []

for i in raw:
  nu = {}
  for k,v in i.items():
    v = v.strip()
    if v.isdigit():
      v = int(v)
    nu[k] = v
  final.append(nu)

print(final)
