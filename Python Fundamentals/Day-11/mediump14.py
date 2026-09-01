'''
### 14. The Stock Portfolio Profit-Loss Engine

Track stock allocations using a dictionary mapping a ticker symbol to a tuple containing (purchase_price, current_price, quantity). Loop through the keys, calculate the net profit or loss for each asset mathematically, and construct a new summary tracking dictionary.
'''

stock = {
    "AAPL": (150.00, 175.00, 10),   # (purchase, current, quantity)
    "GOOGL": (2800.00, 2750.00, 5),
    "TSLA": (700.00, 750.00, 20),
    "AMZN": (3300.00, 3200.00, 3)
}

d = {}

for i in stock:
  purchase = stock[i][0]
  current = stock[i][1]
  quantity = stock[i][2]
  ps_pershare = current - purchase
  ps_total = ps_pershare*quantity
  d[i] = ps_total


print(d)
