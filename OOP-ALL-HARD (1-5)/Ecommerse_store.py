'''
Hard Problem 1 – Integrated E‑Commerce Platform
Context An online marketplace sells physical and digital products. The system must handle product catalogs, customer orders, dynamic discount strategies, and payment processing. It should also track customer loyalty points.

Task Create the following classes:

Product (abstract base)
Attributes: name, price, category (private).
Abstract method: calculate_shipping() – returns shipping cost (0 for digital).
Concrete method: apply_discount(percent) – reduces price.
PhysicalProduct (inherits Product)
Adds: weight (kg) and dimensions (tuple).
Implement: calculate_shipping() as weight * 0.5.
DigitalProduct (inherits Product)
Adds: download_link (private).
Implement: calculate_shipping() returning 0.
Order
Private attributes: __items (list of Product), __customer, __status (pending, paid, shipped).
Methods:
add_item(product, quantity) – store product and quantity.
total_before_discount() – sum of product.price * quantity.
apply_discount_strategy(strategy) – where strategy is a callable (function) that takes the total and returns new total (Strategy pattern).
final_total() – total after discount + shipping (sum of each product’s shipping * quantity).
pay(amount) – if amount >= final_total, mark paid and add loyalty points (1 point per dollar spent) to customer.
Customer
Private: __name, __email, __points (int).
Methods:
add_points(points)
redeem_points(points) (100 points = $1 discount, can be used during checkout).
place_order() – creates an Order and returns it.
DiscountStrategies (static class or separate functions)
percentage_discount(percent) – returns a function that reduces total by percent.
loyalty_discount(points) – returns a function that reduces total by points/100 (capped at total).
free_shipping() – returns a function that subtracts all shipping costs from total (but not below 0).
Additional Requirements

Use @abstractmethod and ABC for Product.
Override __str__ for Product, Order, Customer.
Use a class variable in Product to track total number of products created.
Ensure encapsulation: private attributes with getters where needed.
Sample Usage

# Create products
laptop = PhysicalProduct("Laptop", 1000, "Electronics", weight=2.5)
ebook = DigitalProduct("Python Guide", 30, "Education", link="http://...")

# Create customer
alice = Customer("Alice", "alice@mail.com")

# Place order
order = alice.place_order()
order.add_item(laptop, 1)
order.add_item(ebook, 2)

# Apply discounts
order.apply_discount_strategy(DiscountStrategies.percentage_discount(10))  # 10% off
print(order.final_total())  # (1000+60)*0.9 + shipping(2.5*0.5) = 954 + 1.25 = 955.25

# Pay
order.pay(955.25)
print(alice.get_points())  # 955 points earned (rounded down)
'''


from abc import ABC,abstractmethod

class Product(ABC):
  def __init__(self,name,price,cat):
    self.name = name
    self.price = price
    self.__category = cat

  @abstractmethod
  def calculate_shipping(self):
    pass

  def apply_discount(self,percent):
    discount = self.price * (percent/100)
    self.price-=discount


class PhysicalProduct(Product):
  def __init__(self,name,price,cat,weight,dim=(1,1)):
    super().__init__(name,price,cat)
    self.weight = weight
    self.dimensions = dim

  def calculate_shipping(self):
    return self.weight * 0.5


class DigitalProduct(Product):
  def __init__(self,name,price,cat,link):
    super().__init__(name,price,cat)
    self.__download_link = link

  def calculate_shipping(self):
    return 0.0


class Order():
  def __init__(self,cust):
    self.__items = []
    self.__customer = cust
    self.__status = 'pending'
    self.__strategy = None

  def add_item(self,prod,quan):
    self.__items.append([prod,quan])

  def total_before_discount(self):
    total = 0
    for item,quan in self.__items:
      total+= item.price * quan
    return total 

  def apply_discount_strategy(self,strategy):
    self.__strategy = strategy

  def final_total(self):
    total_price = self.total_before_discount()
    total_shipping = 0
    for item,quan in self.__items:
      if isinstance(item,PhysicalProduct):
        shipping = item.calculate_shipping() * quan
        total_shipping+=shipping

    if self.__strategy is not None:
      final = self.__strategy(total_price,total_shipping)
    else:
      final = total_price

    return final + total_shipping



  def pay(self,amount):
    if amount >= self.final_total():
      self.__status = 'paid'
      self.__customer.add_points(amount/1)
      return True
    return False

  
class Customer():
  def __init__(self,name,email):
    self.__name = name
    self.__email = email
    self.__points = 0

  def add_points(self,points):
    self.__points+=points

  def redeem_points(self,points):
    if self.__points >= points:
      amount = points / 100
      self.__points-=points
      return True
    return False

  def place_order(self):
    return Order(self)

  def get_points(self):
    return self.__points

  
class DiscountStrategies():
  @staticmethod
  def percentage_discount(percent):
    def apply(total,shipping):
      return total * (1-(percent / 100))
    return apply

  @staticmethod
  def loyalty_discount(points):
    def apply(total,shipping):
      return total - (points/100)
    return apply

  @staticmethod
  def free_shipping():
    def apply(total,shipping):
      return total - shipping if total - shipping > 0 else 0
    return apply

