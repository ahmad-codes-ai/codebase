"""
### PROBLEM 3: Shopping Cart Total
Create a function `cart_total()` that:

* Takes a required `tax_rate` (decimal)
* Takes any number of `*prices`
* Takes an optional `discount` defaulting to 0
* Returns total after discount and tax
"""

def cart_total(tax,*prices,discount=0):
  total = 0
  for i in prices:
    total+=i
  total += (total * tax) / 100
  total = total - ((total * discount) /100)

  return f"Final Cart: {total}"


print(cart_total(7,40,10,50,discount=3))
