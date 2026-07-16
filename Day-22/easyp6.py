'''
Problem 6: Car Speed Control
Context: A driving simulator needs car objects.

Task: Create a Car class with:

Attributes: make, model, speed (initial 0).
Methods:
accelerate() – increase speed by 5.
brake() – decrease speed by 5 (not below 0).
display_speed() – print current speed.
Create cars, accelerate/brake, display
'''

class Car:
  def __init__(self,make,model,speed=0):
    self.make = make
    self.model = model
    self.speed = speed 

  def accelerate(self):
    self.speed+=5
    print(f"Your new speed is: {self.speed}")

  def brake(self):
    self.speed-=5
    print(f"Your new speed is: {self.speed}")

  def display_speed(self):
    print(f"Your current speed is: {self.speed}")

c1 = Car('Audi','e4')
c1.accelerate()
c1.accelerate()
c1.display_speed()
c1.brake()