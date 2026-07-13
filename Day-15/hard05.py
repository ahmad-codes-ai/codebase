"""
### 5. System Feature: User Identity Resolution & Engagement Indexer

**Context:** Marketing data is corrupted due to duplicate signups across platforms. The identity resolution microservice must clean, trim, and normalize messy handle metadata strings from three separate networks. The application must discover cross-platform users present in all three databases, merge their independent data records, and compute a consolidated engagement priority index.

**Input State:**
```python
x_net = {"ahmadai": {"followers": 100, "interactions": 5}, "babar_dev": {"followers": 50, "interactions": 1}}
li_net = {"AhmadAI": {"followers": 200, "interactions": 10}, "ali_khan": {"followers": 300, "interactions": 2}}
git_net = {"ahmadai": {"followers": 20, "interactions": 50}}
```

**Expected Output State:**
```python
shared_creators = {"ahmadai"}
master_profiles = {"ahmadai": {"total_followers": 320, "engagement_score": 970}}  # Formula: followers + (interactions * 10)
```
"""

x_net = {"ahmadai": {"followers": 100, "interactions": 5}, "babar_dev": {"followers": 50, "interactions": 1}}
li_net = {"AhmadAI": {"followers": 200, "interactions": 10}, "ali_khan": {"followers": 300, "interactions": 2}}
git_net = {"ahmadai": {"followers": 20, "interactions": 50}}

x = set(i.lower() for i in x_net.keys())
li = set(j.lower() for j in li_net.keys())
git = set(k.lower() for k in git_net.keys())

shared_creators = x & li & git
master_profiles = {}

for i in shared_creators:
  tf = 0
  ti = 0

  for k in x_net.keys():
    if k.lower() == i:
      tf+= x_net[k]['followers']
      ti+= x_net[k]['interactions']
  for k in li_net.keys():
    if k.lower() == i:
      tf+= li_net[k]['followers']
      ti+= li_net[k]['interactions']

  for k in git_net.keys():
    if k.lower() == i:
      tf+= git_net[k]['followers']
      ti+= git_net[k]['interactions']

  eng_score = tf + (ti*10)
  f = {'total_followers': tf, 'engagement_score': eng_score}
  master_profiles[i] = f


print(master_profiles)
