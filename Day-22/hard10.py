"""
### 10. System Feature: SaaS Billing Tier Migration Matrix

**Context:** A company is executing an automated customer migration sweep. The platform management portal requires a script that monitors client lifecycle dictionaries. If an enterprise profile matches specific milestones (months active >= 12 AND API usage > 1000), the engine must modify their tier value fields in-place, apply updated billing prices, and output a roster of modified account IDs.

**Input State:**
```python
users = {"ahmad_dev": {"months": 14, "usage": 1500, "tier": "Standard", "fee": 10}}
```

**Expected Output State:**
```python
updated_users = {"ahmad_dev": {"months": 14, "usage": 1500, "tier": "Premium", "fee": 50}}
notifications = ["ahmad_dev"]
```
"""

users = {
    "ahmad_dev": {"months": 14, "usage": 1500, "tier": "Standard", "fee": 10},
    "fatima_ali": {"months": 18, "usage": 2500, "tier": "Standard", "fee": 10},
    "babar_khan": {"months": 10, "usage": 2000, "tier": "Standard", "fee": 10},
    "sara_ahmed": {"months": 12, "usage": 800, "tier": "Standard", "fee": 10},
    "usman_javaid": {"months": 24, "usage": 1200, "tier": "Standard", "fee": 10}
}

up_users = {}
noti = []

for i in users:
  mo = users[i]['months']
  usg = users[i]['usage']
  if mo >=12 and usg >1000:
    d = {'months': mo, 'usage': usg, 'tier': 'Premeium', 'fee': 50}
    noti.append(i)
  else:
    d = users[i]

  up_users[i] = d

print(noti)
print(up_users)
