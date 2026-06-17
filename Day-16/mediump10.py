'''
### 10. The Cross-Platform Handle Synchronizer

You are pulling developer names from X and LinkedIn. You have two lists of dictionaries containing {"id": handle, "posts": count}. Iterate through both lists simultaneously; merge data for matching handles into a new master dictionary that aggregates total posts across both platforms.
'''

x_data = [
    {"id": "alice_dev", "posts": 150},
    {"id": "bob_coder", "posts": 200},
    {"id": "charlie_ai", "posts": 75}
]

linkedin_data = [
    {"id": "alice_dev", "posts": 45},
    {"id": "saim_te", "posts": 30},
    {"id": "bob_coder", "posts": 80}
]

md = {}
idx = 0
for i in x_data:
  x_id = i['id']
  x_post = i['posts']

  for j in linkedin_data:
    l_id = j['id']
    l_post = j['posts']

    if x_id == l_id :
      md[x_id] = x_post + l_post

print(md)
