class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
      
    def __str__(self):
      return f"Car: {self.brand} going at {self.speed} km/h"


my_car = Car("Toyota", 100)
print(my_car)  