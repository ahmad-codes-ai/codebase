# Problem 22
# The Crypto Price Alert Trigger
# 
# A trading script monitors a sequence of ticker prices. Loop through a list of stock prices; compare each price to the one immediately preceding it in the list, and print "PRICE_DROP" if the current price is lower than the previous one.


p = [100, 102, 101, 105, 98]
max = p[0]
for i in range(0,len(p)):
  if p[i] < p[i-1]:
    print("Price drop")

