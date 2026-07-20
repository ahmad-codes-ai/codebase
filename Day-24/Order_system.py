'''
4. E-Commerce Order with Discount Codes
Context: An online store wants to apply percentage discounts using promo codes.

Task: Create an Order class with:

Attributes: items (list of (item_name, price, quantity)), discount_code (optional).

Methods:

add_item(name, price, qty=1).

apply_discount(code) – if code is valid (use a static method to validate), apply discount percentage (e.g., "SAVE10" = 10% off).

total() – returns total after discount.

Static method: is_valid_code(code) – checks against a hardcoded dictionary of valid codes ({"SAVE10": 0.10, "SAVE20": 0.20}).

Sample Usage:

order = Order()
order.add_item("Laptop", 1000)
order.add_item("Mouse", 20, 2)
order.apply_discount("SAVE10")
print(order.total())  # (1000+40)*0.9 = 936
'''


class Order:
  def __init__(self):
    self.items = []
    self.discount_codes = {"SAVE10": 0.10, "SAVE20": 0.20}
    self.total = 0

  def add_item(self,name,price,qty=1):
    l = [name,price,qty]
    self.items.append(l)
    print('Item added successfully')
    self.total+=price*qty
  
  def total_amount(self):
    return self.total

  def apply_discount(self,code):
    if code in self.discount_codes:
      discount = self.total * self.discount_codes[code]
      self.total-=discount
      print("Discount applied successfully")
    else:
      print("Invalid Code")

order = Order()
order.add_item("Laptop", 1000)
order.add_item("Mouse", 20, 2)
order.apply_discount("SAVE10")
print(order.total_amount())  # (1000+40)*0.9 = 936