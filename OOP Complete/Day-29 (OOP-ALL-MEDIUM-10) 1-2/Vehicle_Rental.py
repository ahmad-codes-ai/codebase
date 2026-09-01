'''
Medium Problem 1 – Vehicle Rental with Insurance.
Context A car rental agency rents out different types of vehicles (cars, bikes, trucks). Each rental requires insurance coverage that varies by vehicle type. The system must calculate rental cost, apply insurance, and handle late returns.

Task Create the following classes:

Vehicle (abstract base)

Attributes: registration, make, model, base_rate_per_day (private).
Abstract method: calculate_insurance() – returns a float.
Concrete method: rental_cost(days) – returns base_rate * days + insurance * days.
Car (inherits Vehicle)

Adds number_of_doors, has_ac (bool).
Insurance = 5% of base_rate.
Bike (inherits Vehicle)

Adds engine_cc, has_helmet (bool).
Insurance = 3% of base_rate.
Truck (inherits Vehicle)

Adds cargo_capacity_kg, axles.
Insurance = 8% of base_rate.
RentalAgreement

Private attributes: __vehicle, __customer, __start_date, __end_date, __actual_return_date.
Methods:
calculate_base_cost() – uses rental_cost(days).
apply_late_fee(rate_per_day) – if actual_return > end_date, charge extra 50% per late day.
generate_invoice() – returns formatted string with all charges.
RentalAgency

Manages __vehicles (list) and __agreements (list).
Methods: add_vehicle(vehicle), rent_vehicle(registration, customer, days), return_vehicle(registration, actual_return_date).
Class variable: LATE_FEE_MULTIPLIER = 1.5.
Static method: validate_license(license_number) – returns True if length == 8.
'''


from abc import ABC, abstractmethod

class Vehicle:
  def __init__(self,regsitration,make,model,rate):
    self.registration = regsitration
    self.make = make
    self.model = model
    self.__rate = rate

  @abstractmethod
  def calculate_insurance(self):
    pass

  def rental_cost(self,days):
    insurance = self.calculate_insurance()
    cost = (self.__rate * days) + (insurance * days)
    return cost

  def get_rate(self):
    return self.__rate


class Car(Vehicle):
  def __init__(self,reg,make,model,rate,doors,ac=False):
    self.doors = doors
    self.ac = ac 
    super().__init__(reg,make,model,rate)

  def calculate_insurance(self):
    return self.get_rate() * 0.05

class Bike(Vehicle):
  def __init__(self,reg,make,model,rate,engine,helmet=False):
    self.engine = engine
    self.helmet = helmet
    super().__init__(reg,make,model,rate)

  def calculate_insurance(self):
    return self.get_rate() * 0.03

class Truck(Vehicle):
  def __init__(self,reg,make,model,rate,cargo,axles):
    self.cargo_cap = cargo
    self.axles = axles
    super().__init__(reg,make,model,rate)

  def calculate_insurance(self):
    return self.get_rate() * 0.08

class RentalAgreement():
  def __init__(self,vehicle,start,end,actual_end):
    self.__vehicle = vehicle
    self.__start_date = start
    self.__end_date = end
    self.__actual_return = actual_end

  def get_vehicle(self):
    return self.__vehicle

  def get_start_date(self):
    return self.__start_date

  def set_return_date(self,date):
    if type(date) == int:
      self.__actual_return = date
      return True
    return False

  def calculate_base_cost(self):
    days = self.__end_date - self.__start_date
    return self.__vehicle.rental_cost(days)

  def apply_late_fee(self,rate,multiplier=1.5):
    if self.__actual_return > self.__end_date:
      extra_days = self.__actual_return - self.__end_date
      return extra_days * (rate*multiplier)
    return 0

  def genrate_invoice(self):
    if self.__actual_return <= self.__end_date:
      return f"You take {self.__vehicle.registration} for rent on day: {self.__start_date} until day {self.__end_date} and returned on day {self.__actual_return} your total bill is: {self.calculate_base_cost()}"
    else:
      return f"You take {self.__vehicle.registration} for rent on day: {self.__start_date} until day {self.__end_date} and returned on day {self.__actual_return} your total combined bill with late_fee is: {self.calculate_base_cost() + self.apply_late_fee(self.__vehicle.get_rate())}"
    
class RentalAgency():

  LATE_FEE_MULTIPLIER = 1.5

  def validate_licence(number):
    if len(number) == 8:
      return True
    return False

  def __init__(self):
    self.vehicles = []
    self.agreements = []

  def add_vehicle(self,vehicle):
    if vehicle not in self.vehicles:
      self.vehicles.append(vehicle)
      return True
    return False
  
  def rent_vehicle(self,registration, customer, days):
    for i in self.vehicles:
      if i.registration == registration:
        agr = RentalAgreement(i,0,0+days,None)
        self.agreements.append(agr)
        return True
    return False

  def return_vehicle(self,reg,return_date):
    for i in self.agreements:
      if i.get_vehicle().registration == reg:
        i.set_return_date(return_date)
        return i.genrate_invoice()
    return False


    
      
#Test Cases 

# # --- 1. FRESH SETUP (Creates everything from scratch) ---
# agency = RentalAgency()

# # Add all vehicles so you don't have to retype later
# car = Car("ABC123", "Toyota", "Camry", 50, 4, True)
# bike = Bike("BIKE99", "Yamaha", "R15", 30, 150, True)
# truck = Truck("TRUCK1", "Volvo", "FH", 100, 2000, 3)

# agency.add_vehicle(car)
# agency.add_vehicle(bike)
# agency.add_vehicle(truck)

# print("--- Setup Complete. Running Test 3 ---")

# # --- 2. EDGE CASE 3: Early Return (Bike) ---
# # Rent for 7 days, return on day 5 (2 days early)
# agreement_bike = agency.rent_vehicle("BIKE99", "Charlie", 7)
# invoice_bike = agency.return_vehicle("BIKE99", 5)
# print(invoice_bike)  # Expected: total = 216.3

# print("\n--- Running Test 4 ---")

# # --- 3. EDGE CASE 4: Late Truck ---
# # Rent for 2 days, return on day 4 (2 days late)
# agreement_truck = agency.rent_vehicle("TRUCK1", "Diana", 2)
# invoice_truck = agency.return_vehicle("TRUCK1", 4)
# print(invoice_truck)  # Expected: total = 516.0


# # Try to return the Car again (already returned in Test 2)
# invoice_again = agency.return_vehicle("ABC123", 10)
# print(invoice_again)  # Should print False (or None), not a number