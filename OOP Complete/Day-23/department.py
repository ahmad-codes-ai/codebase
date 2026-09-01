'''
Problem 14: Department Employee Tracker
Context: A company tracks employees per department.

Task: Create a Department class with:

Attribute: name, employees (list of Employee objects from problem 3).
Methods:
add_employee(emp).
total_salary() – sum of all salaries.
Static method: is_holiday(date) – pretend it always returns False.
Test with employees.

'''


class Employee():

  company_name = 'TechCorp'

  def __init__(self,name,salary=40000):
    self.name = name
    self.sal = salary

  def give_raise(self,p):
    am = (self.sal * p) / 100
    self.sal+=am
    print(f"After a increase of {p}% {self.name}'s new salary is {self.sal}")

  def is_working_day(self,day):
    if day.lower() not in ['saturday','sunday']:
      return True
    else:
      return False

  def change_company_name(name):
    Employee.company_name = name
    print(f"Your new company name is {Employee.company_name}")

class Department:

  def __init__(self,name):
    self.name = name
    self.employess = []
 
  def add(self,emp):
    self.employess.append(emp)
    print(f"{emp.name} is added in {self.name} Department")

  def total_sal(self):
    total = 0
    for emp in self.employess:
      total+=emp.sal
    print(f"Total salary of {self.name} department is = {total}")

  @staticmethod
  def is_holiday(self,date):
    return False

emp1 = Employee('Ahmad',40000)
emp2 = Employee('John',35000)

it = Department('IT')

it.add(emp1)
it.add(emp2)
emp1.give_raise(10)
it.total_sal()