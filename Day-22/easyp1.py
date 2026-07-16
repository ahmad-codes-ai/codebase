'''
Problem 1: Bank Account Simulator
Context: A small bank wants to track customer accounts.

Task: Create a BankAccount class with:

Private attribute __balance (initialised via constructor).
Public attributes: account_holder, account_number.
Methods:
deposit(amount) - add to balance.
withdraw(amount) - subtract only if sufficient funds (print "Insufficient funds" otherwise).
get_balance() - return the current balance (getter).
Create a few accounts, perform deposits/withdrawals, and display balances.

'''


class Bank():
  
  def __init__(self,holder,number):
    self.__bal = 5000
    self.acc_holder = holder
    self.acc_number = number

  def deposit(self,amount):
    if type(amount) == int:
      self.__bal+=amount
      print("Deposit Successfull")
    else:
      print("Plz enter a valid amount")

  def withdraw(self,amount):
    if self.__bal >= amount:
      self.__bal-=amount
      print("Withdraw Successfully")
    else:
      print("You dont have enough money to withdraw")

  def get_bal(self):
    print(f"Your current balance = {self.__bal}")

p1 = Bank('Ahmad',12345)
p1.deposit(4000)
p1.withdraw(3000)
p1.get_bal()