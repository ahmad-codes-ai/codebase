"""
### 2. Incident Report: LLM API Rate Limiter & Budget Exhaustion

Context: A rogue looping agent is draining the startup's LLM API wallet. The credit balance drops rapidly. The system must process an incoming stream of operational dictionaries, compute live micro-costs (input tokens x input cost + output tokens x output cost), update the remaining funds in real-time, and trigger an automated system lock on high-cost models ("gpt-4") the exact millisecond the budget goes into the negative, while permitting low-cost models ("llama-3") to finish their queue.

Input State:
budget = 0.05
costs = {"gpt-4": {"in": 0.01, "out": 0.02}, "llama-3": {"in": 0.002, "out": 0.003}}
logs = [
    {"model": "gpt-4", "in": 2, "out": 1},      
    {"model": "gpt-4", "in": 1, "out": 1},      
    {"model": "gpt-4", "in": 2, "out": 2},      
    {"model": "llama-3", "in": 2, "out": 2}     
]

Expected Output State:
ALERT: Budget depleted! gpt-4 calls frozen.
Final Remaining Budget: -0.03
"""

budget = 0.05
costs = {"gpt-4": {"in": 0.01, "out": 0.02}, "llama-3": {"in": 0.002, "out": 0.003}}
logs = [
    {"model": "gpt-4", "in": 2, "out": 1},
    {"model": "gpt-4", "in": 1, "out": 1},
    {"model": "gpt-4", "in": 2, "out": 2},
    {"model": "llama-3", "in": 2, "out": 2}
]


for i in logs:
  if budget > 0:
    if i['model'] == 'gpt-4':
      cost = (i['in'] * costs['gpt-4']['in']) + (i['out'] * costs['gpt-4']['out'])
      budget-=cost
      if budget < 0:
        print("ALERT: Budget depleted! gpt-4 calls frozen.")
    else:
      cost = (i['in'] * costs['llama-3']['in']) + (i['out'] * costs['llama-3']['out'])
      budget-=cost
      if budget < 0:
        print("ALERT: Budget depleted! gpt-4 calls frozen.")
  else:
    if i['model'] == 'llama-3':
      cost = (i['in'] * costs['llama-3']['in']) + (i['out'] * costs['llama-3']['out'])
      budget-=cost
    else:
      continue



print(f"Final remaining budget: {budget}")


