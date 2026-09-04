'''
Problem 6: User Statistics 📈
You have a file called users.json with this content:

json
[
  {"name": "Alice", "age": 25, "city": "New York"},
  {"name": "Bob", "age": 30, "city": "London"},
  {"name": "Charlie", "age": 35, "city": "New York"},
  {"name": "Diana", "age": 28, "city": "Paris"}
]
Your task:

Read users.json.

Calculate the average age of all users.

Count how many users are from "New York".

Save these statistics to a new file called user_stats.json in this format:

json
{
  "average_age": 29.5,
  "new_york_count": 2
}

'''

import json

with open('users.json','r') as f:
    users = json.load(f)

s = 0
new_yorkers = 0
for user in users:
    s+=user['age']
    if user['city'] == 'New York':
        new_yorkers+=1

avg_age = s / len(users)

data = {
    'average_age': avg_age,
    'new_york_count': new_yorkers
}

with open('user_stats.json','w') as f:
    json.dump(data,f,indent=2)
