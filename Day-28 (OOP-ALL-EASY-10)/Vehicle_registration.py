'''
Easy Problem 8 – Vehicle Registration with Inheritance
Context A DMV system registers vehicles. Cars and motorcycles have different registration fees.

Task Create a Vehicle class with:

Private __plate_number, __owner.
Method: get_registration_fee() – returns a base fee (e.g., 50).
Getters for plate and owner.
Create subclasses:

Car – adds number_of_doors; overrides get_registration_fee() to return 50 + 20 * doors.
Motorcycle – adds engine_cc; overrides get_registration_fee() to return 50 + 0.1 * cc.
Create a DMV class that stores a list of vehicles and computes total fees.

Sample Usage

dmv = DMV()
car = Car("ABC123", "Alice", 4)
bike = Motorcycle("XYZ789", "Bob", 250)
dmv.add_vehicle(car)
dmv.add_vehicle(bike)
print(dmv.total_registration_fees())  # (50+80) + (50+25) = 205
'''


class Vehicle:
  def __init__(self,plate,owner):
    self.__plate_number = plate
    self.__owner = owner

  def get_registration_fee(self):
    return 50

  def get_plate(self):
    return self.__plate_number

  def get_owner(self):
    return self.__owner

class Car(Vehicle):
  def __init__(self,plate,owner,doors):
    self.doors = doors
    super().__init__(plate,owner)

  def get_registration_fee(self):
    return 50 + (20 * self.doors)

class Motorcycle(Vehicle):
  def __init__(self,plate,owner,cc):
    self.engine_cc = cc
    super().__init__(plate,owner)

  def get_registration_fee(self):
    return 50 + (0.1*self.engine_cc)

class DMV:
  def __init__(self):
    self.vehicles = []

  def add_vehicle(self,v):
    if v not in self.vehicles:
      self.vehicles.append(v)
      return True
    return False

  def total_registration_fees(self):
    total = 0
    for i in self.vehicles:
      total+=i.get_registration_fee() 
    return total


dmv = DMV()
car = Car("ABC123", "Alice", 4)
bike = Motorcycle("XYZ789", "Bob", 250)
dmv.add_vehicle(car)
dmv.add_vehicle(bike)
print(dmv.total_registration_fees())  # (50+80) + (50+25) = 205
