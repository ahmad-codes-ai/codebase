'''
Problem 4: Product Discount System
Context: An e‑commerce site needs to apply discounts.

Task: Create a Product class with:

Attributes: name, price (float).
Methods:
apply_discount(percent) – reduce price by percentage.
Static method: apply_tax(price, tax_rate) – return price with tax.
Class variable: tax_rate (default 0.05).
Test with a product, apply discount and tax.
'''


class Product:
  tax_rate = 0.005

  def __init__(self,name,price):
    self.name = name
    self.price = price

  def apply_discount(self,p):
    am = (self.price * p) / 100
    self.price-=am
    print(f"After apllying {p}% discount new price is {self.price}")

  @staticmethod
  def apply_tax(price,tax = tax_rate):
    t = (price*tax)/100
    print(f"Total tax amount: {t}")


p1 = Product('Laptop',7500)
p1.apply_discount(5)
Product.apply_tax(p1.price,2.5)