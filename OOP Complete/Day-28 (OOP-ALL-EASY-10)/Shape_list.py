'''
Easy Problem 9 – Shape Area Calculator (Inheritance)
Context A geometry program computes areas of different shapes.

Task Create a Shape class with:

Method: area() – returns 0 (base).
Create subclasses:

Circle – takes radius, area = π * r² (use math.pi).
Rectangle – takes length and width, area = length * width.
Create a ShapeList class that:

Has a list of Shape objects.
Methods: add_shape(shape), total_area() – sums all areas.
Sample Usage

import math

shapes = ShapeList()
shapes.add_shape(Circle(5))
shapes.add_shape(Rectangle(4, 6))
print(shapes.total_area())  # 78.54 + 24 = 102.54
'''


import math

class Shape:
  
  def area(self):
    return 0

class Circle(Shape):
  def __init__(self,radius):
    self.radius = radius
    
  def area(self):
    return math.pi * (self.radius**2)

class Rectangle(Shape):
  def __init__(self,l,w):
    self.length = l
    self.width = w

  def area(self):
    return self.length * self.width

class ShapeList:
  def __init__(self):
    self.shapes = []

  def add_shape(self,shape):
    if shape not in self.shapes:
      self.shapes.append(shape)
      return True
    return False

  def total_area(self):
    total = 0
    for i in self.shapes:
      total+=i.area()
    return total

shapes = ShapeList()
shapes.add_shape(Circle(5))
shapes.add_shape(Rectangle(4, 6))
print(shapes.total_area())  # 78.54 + 24 = 102.54