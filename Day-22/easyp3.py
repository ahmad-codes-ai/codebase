'''
Problem 3: Employee Salary Manager
Context: A company wants to give raises.

Task: Create an Employee class with:

Attributes: name, salary.
Methods:
give_raise(percentage) - increase salary by percentage.
Static method: is_working_day(day) - return True if day is not Saturday/Sunday.
Class variable: company_name (set to "TechCorp").
Class method: change_company_name(new_name) - update the company name.
Create employees, give raises, check working days.
'''

class Employee():
  
  company_name = 'TechCorp'

  def __init__(self,name,salary=40000):
    self.name = name
    self.sal = salary

  def give_raise(self,p):
    am = (self.sal * p) / 100
    self.sal+=am
    print(f"After a increase of {p}% your new salary is {self.sal}")

  def is_working_day(self,day):
    if day.lower() not in ['saturday','sunday']:
      return True
    else:
      return False

  def change_company_name(name):
    Employee.company_name = name
    print(f"Your new company name is {Employee.company_name}")

e1 = Employee('Ahmad')
e1.give_raise(5)
Employee.change_company_name('Google')
e1.company_name