'''
Medium Problem 6 – Subscription Box Service
Context A company curates subscription boxes (Beauty, Snacks, Books). Customers can subscribe to one or more boxes, and each box has a monthly fee. The system must calculate monthly totals, apply loyalty discounts, and handle box swaps.

Task Create the following classes:

Box (abstract)

Attributes: name, base_price, items (list of item names).
Abstract method: get_description().
BeautyBox – adds brand attribute.

SnackBox – adds dietary_info.

BookBox – adds genre.

Subscription

Private: __customer, __box (Box), __start_date, __active (bool).
Methods: pause(), resume(), upgrade_box(new_box) – replaces the box, pay difference.
Customer

Private: __name, __email, __subscriptions (list of Subscription).
Methods: add_subscription(box), get_monthly_total() – sum of all active box prices.
apply_loyalty_discount(years) – if > 1 year, 5% off; > 3 years, 10% off.
SubscriptionManager

Manages customers and boxes.
Class variable: SHIPPING_COST = 3.99.
Static method: calculate_total(customer) – boxes total + shipping.
Additional

Override __eq__ for Box (based on name and type).
Use __add__ on Customer to merge two customers' subscriptions? Or just a method.
Sample Usage

beauty = BeautyBox("Glow", 30, ["Serum", "Mask"], "L'Oreal")
customer = Customer("Alice", "a@x.com")
customer.add_subscription(beauty)
total = SubscriptionManager.calculate_total(customer)  # 30 + 3.99
print(total)
'''

from abc import ABC, abstractmethod

class Box(ABC):
  def __init__(self,name,base_price,items):
    self.name = name
    self.base_price = base_price
    self.items = items

  @abstractmethod
  def get_description(self):
    pass


class BeautyBox(Box):
  def __init__(self,name,base,items,brand):
    self.brand = brand
    super().__init__(name,base,items)

  def get_description(self):
    s = f"Box Name: {self.name}, Price: {self.base_price} Items: {self.items}"
    return s

class SnackBox(Box):
  def __init__(self,name,base,items,dietry):
    self.dietry_info = dietry
    super().__init__(name,base,items)

  def get_description(self):
    s = f"Box Name: {self.name}, Price: {self.base_price} Items: {self.items}"
    return s

class BookBox(Box):
  def __init__(self,name,base,items,genre):
    self.genre = genre
    super().__init__(name,base,items)

  def get_description(self):
    s = f"Box Name: {self.name}, Price: {self.base_price} Items: {self.items}"
    return s

class Subscription():
  def __init__(self,customer,box,start,active=True):
    self.__customer = customer
    self.__box = box 
    self.__start_date = start
    self.__active = active

  def pause(self):
    if self.__active:
      self.__active = False
      return True
    return False

  def resume(self):
    if not self.__active:
      self.__active = True
      return True
    return False

  def upgrade_box(self,new):
    idx = -1
    nl = self.__customer.get_subscriptions()
    for i in nl:
      idx+=1
      if i == self.__box:
        nl[idx] = new
        return True
    return False



class Customer():
  def __init__(self,name,email):
    self.__name = name
    self.__email = email
    self.__subscriptions = []
    self.discount = None

  def add_subscription(self,box):
    if box not in self.__subscriptions:
      self.__subscriptions.append(box)
      return True
    return False


  def get_subscriptions(self):
    return self.__subscriptions

  def get_monthly_total(self):
    total = 0
    for box in self.__subscriptions:
      total+=box.base_price
    if self.discount is not None:
      discount_amount = total * self.discount
      return total - discount_amount
    return total
  
  def apply_loyalty_discount(self,years):
    if years > 3:
      self.discount = 0.1
      return True
    elif years > 1:
      self.discount = 0.05
      return True
    return False


class SubscriptionManager():

  SHIPPING_COST = 3.99

  @staticmethod
  def calculate_total(customer):
    return customer.get_monthly_total() + SubscriptionManager.SHIPPING_COST


    
