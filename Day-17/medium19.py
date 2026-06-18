"""
Problem 19: The AI Chatbot Chat History Compressor
Long conversations consume model tokens. Take a list of dictionaries representing chat history {"role": "user", "text": "..."}. Loop through the logs; if two consecutive messages are from the same role, combine their text strings together into a single message entry.
"""

result = []
for i in chats:
  if not result:
    result.append(i.copy())
  else:
    if i['role'] == result[-1]['role']:
      result[-1]['text'] = result[-1]['text'] + " " + i['text']
    else:
      result.append({'role': i['role'] , 'text': i['text']})

print(result)
