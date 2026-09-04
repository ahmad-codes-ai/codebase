'''
Problem 9: Nested API Response (Find Most Liked User) 🏆
You have a file called social_data.json with this content (simulating an API response):

json
{
  "data": {
    "users": [
      {
        "name": "Alice",
        "posts": [
          {"title": "Hello World", "likes": 10},
          {"title": "Python tips", "likes": 25}
        ]
      },
      {
        "name": "Bob",
        "posts": [
          {"title": "My day", "likes": 5},
          {"title": "AI is cool", "likes": 30},
          {"title": "Gaming", "likes": 15}
        ]
      },
      {
        "name": "Charlie",
        "posts": [
          {"title": "New bike", "likes": 40}
        ]
      }
    ]
  }
}
Your task:

Read social_data.json.

For each user, calculate their total likes (sum of likes across all their posts).

Find the user with the highest total likes.

Print the result in this format:

text
Charlie has the most likes with 40 total likes.
'''

import json

with open('social_data.json','r') as f:
    data = json.load(f)

d = {}

for user in data['data']['users']:
    likes = 0
    for post in user['posts']:
        likes += post['likes']
    d[user['name']] = likes


highest_likes = max(d, key=d.get)

print(f"{highest_likes} has the highest likes with {d[highest_likes]} total likes")