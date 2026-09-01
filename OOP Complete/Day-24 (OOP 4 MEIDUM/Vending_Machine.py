'''
3. Vending Machine Inventory Manager
Context: A vending machine sells snacks. The machine must track stock and handle purchases.

Task: Create a VendingMachine class with:

Private attribute __inventory – dict mapping item name to [price, stock].

Public methods:

add_item(name, price, stock) – adds or updates an item.

purchase_item(name, money_inserted) – if in stock and money >= price, return change (money - price) and decrease stock; else return None and print error.

check_stock(name) – returns current stock.

get_price(name) – returns price.

Sample Usage:

vm = VendingMachine()
vm.add_item("Coke", 1.50, 5)
vm.add_item("Chips", 1.00, 2)
change = vm.purchase_item("Coke", 2.00)  # returns 0.5, stock becomes 4
print(vm.check_stock("Coke"))  # 4
'''


class VendingMachine():
  def __init__(self):
    self.__inventory = {}

  def add_item(self,name,price,stock):
    if name not in self.__inventory:
      self.__inventory[name] = [price,stock]
      print("Item added")
    else:
      self.__inventory[name] = [price,stock]
      print("Item updated")

  def purchase_item(self,name,price):
    if name in self.__inventory:
      if self.__inventory[name][-1] > 0: 
        if price >= self.__inventory[name][0]:
          self.__inventory[name][-1]-=1
          change = price - self.__inventory[name][0]
          return change
        else:
          return f"Plz Enter money above {self.__inventory[name][0]}"
      else:
        return "Out of stock"
    else:
      return "Item does not exist"

    
  def check_stock(self,name):
    if name in self.__inventory:
      return self.__inventory[name][-1]
    else:
      return "Item does not exist"

  def check_price(self,name):
    if name in self.__inventory:
      return self.__inventory[name][0]
    else:
      return "Item does not exist"

vm = VendingMachine()
vm.add_item("Coke", 1.50, 5)
vm.add_item("Chips", 1.00, 2)
change = vm.purchase_item("Coke", 2.00)  # returns 0.5, stock becomes 4
print(change)
print(vm.check_stock("Coke"))  # 4
