'''
Problem 8: Task Manager (Append to Array) ✅
You have a file called tasks.json with this content:

json
[
  {"id": 1, "description": "Learn Python", "status": "done"},
  {"id": 2, "description": "Learn JSON", "status": "pending"}
]
Your task:

Read tasks.json.

Add a new task with:

id: The next available ID (max existing ID + 1).

description: "Build an AI agent".

status: "pending".

Write the updated list back to tasks.json (overwrite the file) with pretty printing.
'''

import json

with open('tasks.json','r') as f:
    tasks = json.load(f)

for task in tasks:
    last_id = task['id']

next_id = last_id + 1

d = {
    'id':next_id,
    'description': "Build an AI agent",
    'status': 'pending'
}

tasks.append(d)

with open('tasks.json','w') as f:
    json.dump(tasks,f,indent=2)