'''
5. Bank Account with Transaction History
Context: A bank needs to log every transaction for auditing.

Task: Create a BankAccount class with:

Private attributes: __balance, __transaction_history (list of strings like "Deposit: +50").

Methods:

deposit(amount) – add, log "Deposit: +amount".

withdraw(amount) – subtract if sufficient, log "Withdraw: -amount"; else log "Failed withdrawal".

get_balance() – returns balance.

print_history() – prints all transactions.

Sample Usage:
acc = BankAccount("Ahmad", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # fails
acc.print_history()
# Deposit: +50
# Withdraw: -30
# Failed withdrawal
print(acc.get_balance())  # 120
'''

class BankAccount:
    def __init__(self,name,bal):
        self.name = name
        self.__balance = bal
        self.__transaction_history = []

    def deposit(self,amount):
        if amount > 0:
            self.__balance+=amount
            log = f"Deposit: +{amount}"
            self.__transaction_history.append(log)
            return "Deposit Successfully"
        else:
            return "Invalid Input"
        
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance-=amount
            log = f"Withdraw: -{amount}"
            self.__transaction_history.append(log)
            return "Withdraw Successfully"
        else:
            return "Insufficent balance"
        
    def get_balance(self):
        return self.__balance
    
    def print_history(self):
        print(self.__transaction_history)


acc = BankAccount("Ahmad", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  # fails
acc.print_history()
print(acc.get_balance())  # 120