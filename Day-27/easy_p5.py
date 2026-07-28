'''
Problem 5: Vehicle Rental System
Scenario: A rental company manages different types of vehicles.

Task:

Create a base class Vehicle with attributes make, model, and rental_price_per_day.

Create a method calculate_rental_cost(days) that returns the total cost.

Create two subclasses: Car and Motorcycle.

The Car class should have an additional attribute number_of_doors.

The Motorcycle class should have an additional attribute has_sidecar (boolean).

Override the calculate_rental_cost(days) method for Motorcycle to apply a 10% discount for rentals longer than 5 days.
'''


class Vehicle:
  def __init__(self,make,model,price):
    self.make = make
    self.model = model
    self.price = price

  def rental_cost(self,days):
    return self.price * days

class Car(Vehicle):
  def __init__(self,make,model,price,doors):
    self.number_of_doors = doors
    super().__init__(make,model,price)

class Motorcycle(Vehicle):
  def __init__(self,make,model,price,sidecar=False):
    self.has_sidecar = sidecar
    super().__init__(make,model,price)

  def rental_cost(self,days):
    if days > 5:
      cost = (self.price * days) * 0.90
    else:
      cost = self.price * days
    return cost