'''
Medium Problem 4 – Gym Membership with Class Bookings
Context A gym has different membership tiers (Basic, Premium, VIP). Members can book fitness classes (Yoga, Zumba, HIIT). Each class has a capacity. Premium/VIP members get priority booking and discounts.

Task Create the following classes:

Membership (abstract)

Attributes: member_id, name, tier.
Abstract method: get_priority() – returns int (1=Basic, 2=Premium, 3=VIP).
Abstract method: get_discount() – returns percentage off class fees.
BasicMember – priority 1, discount 0%.

PremiumMember – priority 2, discount 10%.

VIPMember – priority 3, discount 20%.

FitnessClass

Attributes: class_name, instructor, capacity, bookings (list of Members).
Methods: book(member) – if space and member not already booked, add; if full, raise exception.
cancel_booking(member) – remove.
get_available_spots().
Gym

Manages classes and members.
Methods: add_class(cls), register_member(member), book_class(member_id, class_name).
Class variable: BASE_CLASS_FEE = 10.
Static method: calculate_fee(member, base) – applies member's discount.
Additional

Override __str__ for members and classes.
Use @property for tier display.
Sample Usage

gym = Gym()
prem = PremiumMember("P001", "Alice")
vip = VIPMember("V002", "Bob")
yoga = FitnessClass("Yoga", "Sara", 2)
gym.add_class(yoga)
gym.register_member(prem)
gym.register_member(vip)
gym.book_class("P001", "Yoga")
gym.book_class("V002", "Yoga")  # capacity 2, both booked
print(yoga.get_available_spots())  # 0
'''


from abc import ABC, abstractmethod

class Membership(ABC):
  def __init__(self,id,name,tier):
    self.member_id = id
    self.name = name
    self.tier = tier.lower().strip()
  
  @abstractmethod
  def get_priority(self):
    pass

  @abstractmethod
  def get_discount(self):
    pass

  def __str__(self):
    return f"Name: {self.name} \n Id: {self.member_id} \n Tier: {self.tier}"


class BasicMember(Membership):
  def __init__(self,id,name,tier='basic'):
    super().__init__(id,name,tier)

  def get_priority(self):
    return 1

  def get_discount(self):
    return None

class PremiumMember(Membership):
  def __init__(self,id,name,tier='premium'):
    super().__init__(id,name,tier)

  def get_priority(self):
    return 2

  def get_discount(self):
    return 0.1

class VIPMember(Membership):
  def __init__(self,id,name,tier='vip'):
    super().__init__(id,name,tier)

  def get_priority(self):
    return 3

  def get_discount(self):
    return 0.2


class FitnessClass:

  def __init__(self,name,instructor,capacity):
    self.class_name = name
    self.instructor = instructor
    self.capacity = capacity
    self.bookings = []

  def book_member(self,mem):
    if len(self.bookings) + 1 <= self.capacity and mem not in self.bookings:
      self.bookings.append(mem)
      return True
    return False

  def __str__(self):
    return f"Class Name: {self.class_name} \n Instructor: {self.instructor} \n Capacity: {self.capacity}"

  def cancel_booking(self,member):
    if member in self.bookings:
      self.bookings.remove(member)
      return True
    return False

  def get_available_spots(self):
    spots = self.capacity - len(self.bookings)
    return spots

class Gym:

    BASE_CLASS_FEE = 10

    @staticmethod
    def calculate_fee(member, base=None):
      if base is None:
        base = Gym.BASE_CLASS_FEE
      if member.get_discount() is not None:
        discount = base * member.get_discount()
        return base - discount
      return base

    def __init__(self):
      self.classes = []
      self.members = []

    def add_class(self,cls):
      if cls not in self.classes:
        self.classes.append(cls)
        return True
      return False

    def register_member(self,mem):
      if mem not in self.members:
        self.members.append(mem)
        return True
      return False

    def book_class(self,member_id,class_name):
      found = False
      idx = -1
      for cls in self.classes:
        idx+=1
        if cls.class_name == class_name:
          found = True
          break
      if not found:
        return False

      for i in self.members:
        if i.member_id == member_id:
          result = self.classes[idx].book_member(i)
          return result
      return False

    def testing(self):
      for i in self.classes:
        print(i.bookings)
  

