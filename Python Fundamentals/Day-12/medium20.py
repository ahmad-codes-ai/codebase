"""
Problem 20: The Crypto Ticker Volatility Monitor
A trading bot analyzes a historical list of pricing float values. Write a loop that flags any instances where the price jumps or drops by more than 15% between two consecutive entries, saving the index positions and directions into a tuple tracking record.
"""

l = []
for i in range(len(prices)-1):
  t = ()
  f = prices[i]
  s = prices[i+1]
  p = ((s - f) / f) * 100
  if abs(p) > 15:
    if p > 0:
      flag = 'UP'
    else:
      flag = 'DOWN'

    t = (i,flag)
    l.append(t)

print(l)
