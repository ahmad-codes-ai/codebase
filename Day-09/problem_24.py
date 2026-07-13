# Problem 24
# The Portfolio Asset Allocator
# 
# A founder's asset values are stored in a dictionary (e.g., {"Cash": 5000, "Stocks": 12000}). Loop through the dictionary keys; if any asset category holds more than 10,000 in value, print that category name alongside a "Heavy Investment" label.


assets = {
    "Cash": 5000,
    "Stocks": 12000,
    "Bonds": 8000,
    "Real Estate": 25000,
    "Crypto": 15000,
    "Commodities": 4000,
    "Mutual Funds": 9500
}

for (key,value) in assets.items():
  if value > 10000:
    print(f"{key} : Heavy Investment")

