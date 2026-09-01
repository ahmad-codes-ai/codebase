'''
Problem 2: Inventory Management
Scenario: A warehouse stores different types of items.

Task:

Create a base class Item with attributes name, price, and quantity_in_stock.

Create a method total_value() that returns the total value of the item in stock (price * quantity).

Create two subclasses: Electronics and Groceries.

The Electronics class should have an additional attribute warranty_period (in months).

The Groceries class should have an additional attribute expiry_date (as a string, e.g., "2024-12-31").

For each subclass, create a method restock() that adds a specified amount to quantity_in_stock.
'''


class Item:
  def __init__(self,name,price,stock):
    self.name = name
    self.price = price
    self.stock = stock

  def total_value(self):
    return self.price * self.stock

class Electronics(Item):
  def __init__(self,name,price,stock,waar):
    self.warrenty = waar
    super().__init__(name,price,stock)

  def restock(self,quan):
    self.stock += quan


class Groceries(Item):
  def __init__(self,name,price,stock,exp):
    self.expiry = exp
    super().__init__(name,price,stock)

  def restock(self,quan):
    self.stock += quan