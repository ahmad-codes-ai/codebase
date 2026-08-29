'''
Hard Problem 4 – Ride‑Sharing Platform with Dynamic Pricing
Context A ride‑sharing app connects drivers and riders. Fares depend on distance, time of day, and demand (surge pricing). The system must handle trip tracking, driver ratings, and payment splitting.

Task Create the following classes:

User (abstract)
Attributes: user_id, name, phone (private).
Abstract method: get_type() – returns "rider" or "driver".
Rider (inherits User)
Adds: payment_methods (list), trip_history.
Methods: request_ride(pickup, dropoff, driver_preference=None).
Driver (inherits User)
Adds: vehicle, license, rating (float), is_available.
Methods:
accept_ride(trip)
complete_trip(trip)
update_rating(new_rating)
Trip
Private attributes: __rider, __driver, __pickup, __dropoff, __distance_km, __start_time, __end_time, __fare (float).
Methods:
calculate_fare() – uses dynamic pricing (base rate + distance * per_km + time_factor based on hour).
apply_surge(factor) – multiplies fare by factor.
split_fare(rider_list) – returns dict with per‑rider share.
complete() – sets end time, updates driver availability, adds to history.
RideSharingService
Manages: lists of riders, drivers, trips.
Methods:
add_user(user)
match_driver(rider) – finds nearest available driver (simulate).
request_trip(rider, pickup, dropoff) – creates Trip, matches driver, calculates fare.
get_earnings(driver) – total fare of completed trips.
Additional Requirements

Use ABC.
Override __str__ and __repr__.
Use class variables to track total trips, total earnings.
Use static method to validate phone numbers.
Override __lt__ to compare drivers by rating for sorting.
'''



from abc import ABC,abstractmethod

class User(ABC):
  def __init__(self,id,name,phone):
    self.user_id = id
    self.name = name
    self.__phone = phone

  @abstractmethod
  def get_type(self):
    pass


class Rider(User):
  def __init__(self,id,name,phone,payment_method):
    super().__init__(id,name,phone)
    self.payment_method = payment_method
    self.trip_history = []

  def get_type(self):
    return 'rider'

  def request_ride(self,pick,drop,rider_pref=None):
    return [pick,drop]


class Driver(User):
  def __init__(self,id,name,phone,vehicle,licence,rating=0.0,is_available=True):
    super().__init__(id,name,phone)
    self.vehicle = vehicle 
    self.licence_no = licence
    self.rating = rating
    self.is_available = is_available
    self.earnings = 0.0
    self.current_location = 'A'
    self.history = []

  
  def get_type(self):
    return 'driver'

  def accept_ride(self,trip):
    if self.is_available:
      self.is_available = False
      return True
    return False

  def complete_trip(self,trip):
    self.is_available = True
    self.current_location = trip.get_drop_off()

  def update_rating(self,new_rating):
    self.rating = new_rating

  def add_earning(self,earning):
    self.earnings+=earning 


class Trip():

  locations_distance = {
        ('A','B') : 5.4,
        ('B','A') : 5.4,
        ('B','C') : 4.2,   
        ('C','B') : 4.2,
        ('A','C') : 9.6,
        ('C','A') : 9.6
    }

  time_factor = {
        ("00","06") : 0.80,
        ('07','12') : 1.10,
        ('13','18') : 1.20,
        ('19','24') : 1.00,
    }

  def __init__(self,rider,driver,pickup,drop_off,start_time):
    self.__rider = rider
    self.__driver = driver
    self.__start_time = start_time
    self.__pickup = pickup
    self.__drop_off = drop_off
    self.__fare = 0.0
    self.time_factor = 1.0



    hour = self.__start_time[0]
    for k,v in Trip.time_factor.items():
      first,last = k[0],k[1]
      for i in range (int(first),int(last)+1):
        if hour == i:
          self.time_factor = v 

    self.location = (self.__pickup,self.__drop_off)
    self.__distance = Trip.locations_distance.get(self.location,None)
    self.time_taken = (self.__distance * 4)  
    self.__end_time = f"{self.__start_time[0:2]}:{str( int(self.__start_time[-2:]) + int(self.time_taken) )}"
    self.calculate_fare()


  def calculate_fare(self):
    base = 5
    per_km = 2
    final = base + ( (self.__distance * per_km) * self.time_factor ) 
    self.__fare = final 
    return self.__fare 

  def apply_surge(self,factor):
    self.__fare = self.__fare * factor
    return self.__fare

  def split_fare(self,rider_list):
    l = len(rider_list)
    per_person = self.__fare / l

    for rider in rider_list:
      d = {rider:per_person}

    return d

  def complete(self):
    self.__driver.complete_trip(self)
    self.__driver.add_earning(self.__fare)
    details_d = f"Pickup: {self.__pickup} , Drop: {self.__drop_off} , time_taken: {self.time_taken} , Earning: {self.__fare}"
    self.__driver.history.append(details_d)
    details_r = f"Pickup: {self.__pickup} , Drop: {self.__drop_off}, Paid: {self.__fare}"
    self.__rider.trip_history.append(details_r)
    self.__driver.update_rating(self.__driver.rating + 0.5)

  def get_drop_off(self):
    return self.__drop_off


class RideSharingService():
  def __init__(self):
    self.riders = []
    self.drivers = []

  def add_rider(self,rider):
    if rider not in self.riders:
      self.riders.append(rider)
      return True
    return False

  def add_driver(self,driver):
    if driver not in self.drivers:
      self.drivers.append(driver)
      return True
    return False

  def match_driver(self,rider,pick,drop):
    final_driver = None
    small_distance = 100
    for driver in self.drivers:
      if driver.is_available:
        driver_location = driver.current_location
        distance = Trip.locations_distance.get((driver_location,drop),None)
        if distance is None:
          return None
        if distance < small_distance:
          small_distance = distance
          final_driver = driver
    return final_driver

  def request_trip(self,rider,pickup,dropoff,start_time):
    driver = self.match_driver(rider,pickup,dropoff)
    if driver is None:
      return False
    t = Trip(rider,driver,pickup,dropoff,start_time)
    return t

  def get_earnings(self,driver):
    for d in self.drivers:
      if d == driver:
        return d.earnings
    return False




# Test cases 


print("=" * 40)
print("TEST 1: Create Riders and Drivers")
print("=" * 40)

rider1 = Rider("R123", "Alice", "123-456-7890", ["Credit Card"])
rider2 = Rider("R456", "Bob", "987-654-3210", ["PayPal"])
driver1 = Driver("D789", "Charlie", "111-222-3333", "Tesla", "LIC123", rating=4.5)
driver2 = Driver("D999", "Diana", "444-555-6666", "BMW", "LIC456", rating=4.8)

service = RideSharingService()
service.add_rider(rider1)
service.add_rider(rider2)
service.add_driver(driver1)
service.add_driver(driver2)

print(f"Riders added: {len(service.riders)}")
print(f"Drivers added: {len(service.drivers)}")

print("\n" + "=" * 40)
print("TEST 2: Request Trip 1 (Rider1 from A to B at 10:00)")
print("=" * 40)

trip1 = service.request_trip(rider1, "A", "B", "10:00")
print(f"Trip created: {trip1 is not None}")

print("\n" + "=" * 40)
print("TEST 3: Complete Trip 1 and Check Earnings")
print("=" * 40)

trip1.complete()
print(f"Driver earnings: ${service.get_earnings(driver1)}")
print(f"Driver location after trip: {driver1.current_location}")
print(f"Driver available: {driver1.is_available}")

print("\n" + "=" * 40)
print("TEST 4: Request Trip 2 (Rider2 from B to C at 15:30)")
print("=" * 40)

trip2 = service.request_trip(rider2, "B", "C", "15:30")
print(f"Trip created: {trip2 is not None}")

print("\n" + "=" * 40)
print("TEST 5: Complete Trip 2 and Check Earnings")
print("=" * 40)

trip2.complete()
print(f"Driver earnings: ${service.get_earnings(driver1)}")
print(f"Driver location after trip: {driver1.current_location}")

print("\n" + "=" * 40)
print("TEST 6: Trip History for Rider1 and Driver1")
print("=" * 40)

print(f"Rider1 trip history: {len(rider1.trip_history)}")
print(f"Driver1 trip history: {len(driver1.history)}")

print("\n" + "=" * 40)
print("TEST 7: Get Fare for Trip 1 and Trip 2")
print("=" * 40)

print(f"Trip 1 fare (A to B): ${trip1._Trip__fare:.2f}")
print(f"Trip 2 fare (B to C): ${trip2._Trip__fare:.2f}")