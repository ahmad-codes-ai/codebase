'''' 
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details. Give the complete code for the BankAccount class.
'''


class Bank:
  
  def __init__(self,number,name,bal):
    self.number = number
    self.name = name
    self.bal = bal
    self.fee = 0.5
  def deposit(self,am):
    self.bal+=am

  def withdraw(self,am):
    self.bal-=am

  def bankfee(self):
    total = self.bal * self.fee
    sub = self.bal - total
    self.bal-=sub

  def show(self):
    print(f''' 
    Account Number: {self.number}
    Account Name: {self.name}
    Account Balance: {self.bal}''')

user1 = Bank(1001,'Ahmad',10000)
user1.deposit(700)
user1.show()
user1.withdraw(7000)
user1.show()

  