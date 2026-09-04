'''
Problem 5: Config Updater ⚙️
You have a file called config.json with this content:

json
{
  "theme": "light",
  "language": "en",
  "notifications": true,
  "volume": 80,
  "auto_save": false
}
Your task:

Read config.json.

Change theme to "dark".

Change volume to 100.

Save the updated config back to the same file (config.json) with pretty printing (indent=2).
'''

import json

with open('config.json','r') as f:
    data = json.load(f)
    data['theme'] = 'dark'
    data['volume'] = 100

with open('config.json','w') as f:
    json.dump(data,f,indent=2)