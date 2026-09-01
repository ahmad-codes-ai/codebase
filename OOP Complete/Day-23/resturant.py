'''
Problem 12: Restaurant Menu Order
Context: A restaurant needs to place orders.

Task: Create a Restaurant class with:

Attribute: menu (dict: item -> price).
Methods:
add_to_menu(item, price).
place_order(items) – items is a list of item names, returns total cost (print unavailable items).
Create a menu, place orders.
'''


class Resturant:
  
  def __init__(self):
    self.menu = {'rice':4, 'chicken':9.5, 'beef': 12.5}

  def add_to_menu(self,name,p):
    if name not in self.menu:
      self.menu[name] = p
    else:
      print("Item already exist")

  def show(self):
    print(self.menu)

  def place_order(self,items):
    total = 0
    for i in items:
      if i in self.menu:
        total+=self.menu[i]
      else:
        print(f"{i} not in menu")
    print(f"Your tottal bill is = {total}")

r1 = Resturant()
r1.add_to_menu('alo',5)
r1.show()
r1.place_order(['rice','beef'])