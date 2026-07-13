"""
Problem 21: The CRM Subscription Renewal Flag
A client roster maps usernames to a nested data dictionary containing {"days_left": int, "auto_renew": bool}. Iterate through the roster; extract users who have less than 7 days left and have auto_renew set to False into an urgent actions list.
"""

alert = []

for i in roster:
  renew = roster[i]['auto_renew']
  if renew == False:
    days = roster[i]['days_left']
    if days < 7:
      alert.append(i)

print(alert)
