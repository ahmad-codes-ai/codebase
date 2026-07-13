"""
### 1. System Feature: AI Orchestrator Prompt Routing Engine

Context: The production gateway receives unformatted user prompts. The system must inspect the string payloads, classify them into the correct agent routing queue based on operational keywords (fetch -> Scraper, draft -> Writer, debug -> Reviewer), scan for urgent escalation triggers (URGENT or !), and isolate unclassifiable traffic into a dead-letter fallback array.

Input State:
raw_prompts = ["URGENT: fetch analytics data!", "draft a blog post", "debug my nested loop login system", "say hello world"]

Expected Output State:
{
    "Scraper_Agent": [{"task": "URGENT: fetch analytics data!", "priority": "high"}],
    "Writer_Agent": [{"task": "draft a blog post", "priority": "low"}],
    "Reviewer_Agent": [{"task": "debug my nested loop login system", "priority": "low"}],
    "Fallback": [{"task": "say hello world", "priority": "low"}]
}
"""

raw_prompts = ["URGENT: fetch analytics data!", "draft a blog post", "debug my nested loop login system", "say hello world"]

routing_dict = {
    "Scraper_Agent": [],
    "Writer_Agent": [],
    "Reviewer_Agent": [],
    "Fallback": []
}


for i in raw_prompts:
  if 'fetch' in i:
    if '!' in i or 'URGENT' in i:
      p = 'high'
    else:
      p = 'low'
    d = {}
    d['task'] = i
    d['priority'] = p
    routing_dict['Scraper_Agent'].append(d)

  elif 'draft' in i:
    if '!' in i or 'URGENT' in i:
      p = 'high'
    else:
      p = 'low'
    d = {}
    d['task'] = i
    d['priority'] = p
    routing_dict['Writer_Agent'].append(d)

  elif 'debug' in i:
    if '!' in i or 'URGENT' in i:
      p = 'high'
    else:
      p = 'low'
    d = {}
    d['task'] = i
    d['priority'] = p
    routing_dict['Reviewer_Agent'].append(d)

  else:
     if '!' in i or 'URGENT' in i:
      p = 'high'
     else:
      p = 'low'
     d = {}
     d['task'] = i
     d['priority'] = p
     routing_dict['Fallback'].append(d)

print(routing_dict)
