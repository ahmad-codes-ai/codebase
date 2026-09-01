'''
Problem 9: Order Calculator
Context: A shopping cart needs to calculate total.

Task: Create an Order class with:

Attributes: items (list of (name, price, quantity)).
Methods:
add_item(name, price, qty=1).
total() – sum of price*qty.
Static method: shipping_cost(total) – if total < 50, return 5; else return 0.
Create an order, add items, print total and shipping.
'''


class Order:

  def __init__(self):
    self.items = []

  def add(self,n,p,q):
    self.name = n
    self.price = p
    self.quan = q
    self.items.extend([self.name,self.price,self.quan])
    print(self.items)
  
  def total(self):
    t = self.price * self.quan
    return t

  @staticmethod
  def shipping(t):
    total = t
    if total < 50:
      return 5
    else:
      return 0

o1 = Order()
o1.add('xyz',100,3)
s = o1.total()
print(s)
Order.shipping(o1.total())   