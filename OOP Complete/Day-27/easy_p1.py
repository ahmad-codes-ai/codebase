'''
Problem 1: Employee Management
Scenario: A company needs to manage its employees.

Task:

Create a base class Employee with attributes name, employee_id, and salary.

Create a method display_info() that prints all the employee's details.

Create two subclasses: Manager and Developer.

The Manager class should have an additional attribute team_size.

The Developer class should have an additional attribute programming_language.

Override the display_info() method in both subclasses to include their specific attributes.

Create instances of each class and call their display_info() method.
'''


class Employee:
  def __init__(self,name,id,sal):
    self.name = name
    self.id = id
    self.sal = sal
  
  def display_info(self):
    return f"Name: {self.name} Id: {self.id} Salary: {self.sal}"

class Manager(Employee):
  def __init__(self,name,id,sal,team):
    super().__init__(name,id,sal)
    self.team = team

  def display_info(self):
    print(f"{super().display_info()} Team: {self.team}")

class Developer(Employee):
  def __init__(self,name,id,sal,lang):
    super().__init__(name,id,sal)
    self.lang = lang

  def display_info(self):
    print(f"{super().display_info()} lang: {self.lang}")

dev = Developer('Ahmad',101,100,'Pyhton')
dev.display_info()

man = Manager('Ali',1001,200,12)
man.display_info()

emp = Employee('Zara',1002,150)
print(emp.display_info())
