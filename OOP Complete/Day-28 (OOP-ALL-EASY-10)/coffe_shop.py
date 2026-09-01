'''
Easy Problem 2 – Coffee Shop Order
Context A coffee shop sells different drinks. Customers place orders, and the shop can apply a weekday discount.

Task Create a Coffee class with:

Attributes: size (small/medium/large), type (e.g., latte), price.
Create an Order class that:

Has a list of Coffee objects.
Methods: add_coffee(coffee), total() – sum of prices.
Static method: apply_weekday_discount(total) – if today is weekday (pretend always True), apply 10% discount.
Class variable: DISCOUNT_RATE = 0.10.
Sample Usage

order = Order()
order.add_coffee(Coffee("medium", "Latte", 4.5))
order.add_coffee(Coffee("small", "Espresso", 3.0))
total = order.total()
discounted = Order.apply_weekday_discount(total)
print(discounted)  # 6.75
'''

class Coffee:
  def __init__(self,size,c_type,price):
    self.size = size
    self.c_type = c_type
    self.price = price

class Order:

  DISCOUNT_RATE = 0.10

  def __init__(self):
    self.coffees = []

  def add_coffee(self,cof):
    if cof not in self.coffees:
      self.coffees.append(cof)
      return True
    else:
      return False

  def total(self):
    t = 0
    for i in self.coffees:
      t+= i.price
    return t

  def apply_weekday_discount(total):
      discount = total * Order.DISCOUNT_RATE
      return total - discount

order = Order()
order.add_coffee(Coffee("medium", "Latte", 4.5))
order.add_coffee(Coffee("small", "Espresso", 3.0))
total = order.total()
discounted = Order.apply_weekday_discount(total)
print(discounted)  # 6.75    