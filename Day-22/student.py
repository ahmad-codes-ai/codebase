'''
Problem 2: Student Grade Tracker
Context: A school needs a system to store student marks.

Task: Create a Student class with:

Attributes: name, grades (list of numbers).
Methods:
add_grade(grade) - append a grade.
average() - return the average of grades.
report() - print name and average.
Create a student, add grades, print the report.
'''


class Student():

  def __init__(self,name,grades=[]):
    self.name = name
    self.grades = grades

  def add_grade(self,grade):
    if type(grade) == int:
      self.grades.append(grade)
      print("Grade added successfully")
    else:
      print("Invalid Input")

  def average(self):
    s = sum(self.grades)
    avg = s/len(self.grades)
    print(f"{self.name} has a average grade of {avg}")
    return avg

  def report(self):
    print(f"Student name: {self.name}")
    print(f"Grades: {self.grades}")
    print(f"Average grade: {self.average()}")

s1 = Student('Ahmad',[100,29,37,43])
s1.average()
s1.add_grade(40)
s1.report()