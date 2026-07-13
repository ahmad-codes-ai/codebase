# Problem 32
# The E-Commerce Price Incrementor
# 
# Due to inflation, an online store needs to raise prices across a whole product catalog. Take a list of product prices as float values, loop through the items, increment each price by exactly 5% in place, and output the updated list.


prices = [19.99, 45.50, 9.99, 99.00, 12.75, 199.99, 4.50, 29.99, 149.00, 7.25]
for i in range(0,len(prices)):
    prices[i] = prices[i] * 1.05

print(prices)

