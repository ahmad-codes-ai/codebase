'''
Medium Problem 8 – Food Delivery Platform
Context A food delivery app connects restaurants, drivers, and customers. Orders have items, delivery fees, and tip options. Restaurants have ratings.

Task Create the following classes:

Restaurant

Attributes: name, menu (dict: item -> price), rating (float).
Methods: add_item(name, price), update_rating(new_rating).
Driver

Private: __name, __vehicle, __current_order (Order or None).
Methods: accept_order(order), complete_order(), is_available().
Order

Private: __customer, __restaurant, __items (list of (item, qty)), __status (pending, assigned, delivered).
Methods: add_item(item, qty), total_before_tip(), apply_tip(amount).
assign_driver(driver).
final_total(delivery_fee) – items + delivery + tip.
DeliveryPlatform

Manages restaurants, drivers, orders.
Methods: register_restaurant(rest), register_driver(driver).
place_order(customer, restaurant_name, items) – creates Order.
assign_driver_to_order(order) – finds first available driver.
Static method: calculate_delivery_fee(distance_km) –  2base+ 0.5/km.
Additional

Use class variable ORDER_COUNTER for unique order IDs.
Override __str__ for Order to show receipt.
Sample Usage

platform = DeliveryPlatform()
rest = Restaurant("Pizza Hut", {"Margherita": 10, "Pepperoni": 12})
platform.register_restaurant(rest)
driver = Driver("Bob", "Scooter")
platform.register_driver(driver)
order = platform.place_order("Alice", "Pizza Hut", [("Margherita", 2)])
platform.assign_driver_to_order(order)
order.apply_tip(3)
print(order.final_total(platform.calculate_delivery_fee(5)))  # 20 + 4.5 + 3 = 27.5
'''

class Resturant:
  def __init__(self,name,menu={},rating=0):
    self.name = name
    self.menu = menu
    self.rating = rating

  def add_item(self,name,price):
    self.menu[name] = price

  def update_rating(self,new_rating):
    self.rating = new_rating 

class Driver:
  def __init__(self,name,vehicle):
    self.__name = name
    self.__vehicle = vehicle
    self.__current_order = None

  def accept_order(self,order):
    if self.__current_order is None:
      self.__currrent_order = order
      return True
    return False

  def complete_order(self):
    if self.__current_order is not None:
      self.__current_order.change_status('delivered')
      self.__current_order = None
      return True
    return False


  def is_available(self):
    if self.__current_order is None:
      return True
    return False

  
class Order:
  def __init__(self,customer,resturant,items):
    self.__customer = customer
    self.__resturant = resturant
    self.__items = []
    self.__status = 'pending'
    self.total_bill = 0

  def add_item(self,item,quan):
    t = (item,quan)
    self.__items.append(t)

  def change_status(self,ns):
    self.__status = ns

  def total_before_tip(self):
    total = 0
    for item,quan in self.__items:
      if item in self.__resturant.menu:
        price = self.__resturant.menu.get(item,'No item exist')
        price_total = price * quan
        total+=price_total
    self.total_bill = total
    return total

  def aplly_tip(self,amount):
    self.total_bill+=amount

  def assign_driver(self,driver):
    if driver.is_available():
      driver.accept_order(self)
      return True
    return False

  def final_total(self,fee):
    self.total_bill += fee
    return self.total_bill

  