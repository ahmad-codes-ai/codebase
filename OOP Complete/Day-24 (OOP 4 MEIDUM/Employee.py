'''
2. Employee Payroll with Overtime
Context: A company pays employees a base salary plus overtime (1.5× hourly rate for hours over 40 per week).

Task: Create an Employee class with:

Attributes: name, base_salary (yearly), hours_worked (weekly hours).

Methods:

calculate_monthly_pay() – base salary / 12 + overtime pay (hours > 40 => extra hours * 1.5 * hourly_rate, where hourly_rate = base_salary / (52 * 40)).

Class variable: company_name = "TechCorp".

Static method: is_weekend(day) – returns True if day is "Saturday" or "Sunday".

Class method: change_company_name(new_name).

Sample Usage:

emp = Employee("Bob", 60000, 45)  # base 60k, 45 hrs/week
print(emp.calculate_monthly_pay()) # ~ 5000 + overtime
print(Employee.is_weekend("Saturday")) # True
Employee.change_company_name("AI Corp")
'''


class Employee:
  company_name = "TechCorp"
  def __init__(self,name,base,hours):
    self.name = name
    self.base = base
    self.hours = hours

  def calculate_monthly_pay(self):
    if self.hours <= 40:
      ms = self.base / 12
    else:
      hour_rate = self.base / (52*40)
      extra = self.hours - 40
      extra_money = extra * (hour_rate * 1.5)
      ms = (self.base + extra_money) / 12
    return ms

  @staticmethod
  def is_weekend(day):
    if day.lower().strip() in ['saturday','sunday']:
      return True
    else:
      return False

  def change_company_name(name):
    Employee.company_name = name
    print("Company name changed successfully")

emp = Employee("Bob", 60000, 45)  # base 60k, 45 hrs/week
print(emp.calculate_monthly_pay()) # ~ 5000 + overtime
print(Employee.is_weekend("Saturday")) # True
Employee.change_company_name("AI Corp")
