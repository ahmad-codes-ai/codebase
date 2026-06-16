"""
### 5. The SaaS Multi-Tier Billing Calculator

A user profile database is structured as a dictionary of dictionaries, holding user tiers and usage counts: {"user1": {"tier": "Pro", "requests": 1500}}. Loop through the users; calculate their final monthly invoice using a fixed base rate plus overage multipliers based on their tier rules.

Basic: Base fee = $10, Free requests = 100, Overage = $0.10 per extra request
Pro: Base fee = $50, Free requests = 1000, Overage = $0.05 per extra request
Enterprise: Base fee = $200, Free requests = 5000, Overage = $0.02 per extra request
"""

users = {
    "user1": {"tier": "Basic", "requests": 120},
    "user2": {"tier": "Pro", "requests": 1500},
    "user3": {"tier": "Enterprise", "requests": 5000},
    "user4": {"tier": "Basic", "requests": 250},
    "user5": {"tier": "Pro", "requests": 1800}
}

d = {}
basic = 0.10
pro = 0.05
enterprise = 0.02

for i,j in users.items():
  if users[i]['tier'] == 'Basic':
    if users[i]['requests'] > 100:
      m = users[i]['requests'] - 100
      m = m * basic
      d[i] = m + 10
    else:
      d[i] = 10

  elif users[i]['tier'] == 'Pro':
    if users[i]['requests'] > 1000:
      m = users[i]['requests'] - 1000
      m = m * pro
      d[i] = m + 50
    else:
      d[i] = 50

  elif users[i]['tier'] == 'Enterprise':
    if users[i]['requests'] > 5000:
      m = users[i]['requests'] - 5000
      m = m * enterprise
      d[i] = m + 200
    else:
      d[i] = 200

print(d)
