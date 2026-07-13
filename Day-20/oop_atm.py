class Atm:
  def __init__(self) :
     self.balance = 10000
     self.pin = ''
     self.menu()

  def menu(self):
    user = int(input(''' 
    1. Create a pin
    2. Change pin
    3. See balance
    4. Withdraw balance
    5. Exit
    Enter your choice'''))

    if user == 1:
      self.create_pin()
    elif user == 2:
      self.change_pin()
    elif user == 3:
      self.show_balance()
    elif user == 4:
      self.withdraw_balance()
    elif user == 5:
      self.exit()

  def create_pin(self):
    p = input("Enter your pin: ")
    self.pin = p
    print("Pin created successfully")
    self.menu()
  
  def change_pin(self):
    p = input("Enter your current pin: ")
    if p == self.pin:
      np = input("Enter your new pin: ")
      self.pin = np
      print("Pin changed successfully")
      self.menu()
    else:
      print("Wrong pin entered")
      self.menu()

  def show_balance(self):
    print(f"Your current balance is : {self.balance}")
    self.menu()

  def withdraw_balance(self):
    amount = int(input("Enter the amount you want to withdraw: "))

    if self.balance > amount or self.balance == amount:
      self.balance-=amount
      print(f"You have successfully withdraw {amount} amount")
      self.menu()
    else:
      print(f"Your current balance {self.balance} is low then the amount you need")
      self.menu()

  def exit(self):
    print("Thanks for using this system")