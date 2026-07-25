'''
1. Banking System with Fraud Detection
Context: A bank wants to detect suspicious activity on customer accounts. Each account has a transaction history. The system must flag accounts where the total withdrawal amount in the last 24 hours exceeds a certain threshold (e.g., $10,000) or if there are more than 5 withdrawals in an hour.
Task: Create three classes:
Transaction: with attributes amount, type ("deposit" or "withdrawal"), timestamp (simulate with a simple integer or string for simplicity).

BankAccount: with private __balance, private __transactions (list of Transaction objects). Methods: deposit(amount), withdraw(amount), get_balance(), get_transactions(). Also a private method _add_transaction(amount, type).

FraudDetector: a utility class with static methods:

check_withdrawal_limit(account, limit=10000, hours=24) – returns True if total withdrawals in last hours exceed limit.
check_frequency(account, max_withdrawals=5, minutes=60) – returns True if more than max_withdrawals withdrawals occurred in the last minutes minutes.
(For simplicity, you can store timestamps as integers representing minutes since epoch, or just use a simple counter.)

Additional Requirement: The BankAccount class should have a class variable daily_withdrawal_limit that can be updated globally. Also add a class method to set that limit.
Sample Usage:
# Create account
acc = BankAccount("Alice", 5000)
acc.deposit(1000)
acc.withdraw(200)
acc.withdraw(300)
# Assume we have timestamps; for testing, we can manually add transactions with fake times.
# Then use FraudDetector checks.
if FraudDetector.check_withdrawal_limit(acc, 500, 1):
    print("Alert: high withdrawal in last hour")
'''

class Transaction:
    def __init__(self,amount,type,timestamp):
        self.amount = amount
        self.type = type
        self.time = timestamp

class BankAccount:
    daily_withdrawal_limit = 50000

    def set_daily_limit(limit):
        BankAccount.daily_withdrawal_limit = limit
        
    def __init__(self,name,bal):
        self.name = name
        self.__balance = bal
        self.__transactions = []
        self.daily_withdraw = 0

    def __add_transaction(self, amount, type , time):
        t = Transaction(amount,type,time)
        self.__transactions.append(t)

    def deposit(self,amount,time):
        t = Transaction(amount,'Deposit',time)
        self.__balance+=amount
        self.__transactions.append(t)

    def withdraw(self,amount,time):
        if self.__balance >= amount and self.daily_withdraw + amount < self.daily_withdrawal_limit:
            t = Transaction(amount,'Withdraw',time)
            self.__transactions.append(t)
            self.daily_withdraw+=amount
            self.__balance-=amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

class FraudDetector:

    @staticmethod
    def check_withdrawal_limit(account, limit=10000, hours=24):
        trans = account.get_transactions()
        max_time = 0
        total = 0
        for i in trans:
            if i.time > max_time:
                max_time = i.time

        min_time = 0

        if max_time - hours < 0:
            pass
        else:
            min_time = max_time - hours

        for t in trans:
            if t.type == 'Withdraw' and t.time >= min_time and t.time <= max_time :
                total+=t.amount

        if total > limit:
            return True
        else:
            return False

    @staticmethod
    def check_frequency(account, max_withdrawals=5, hours=1):
        trans = account.get_transactions()
        max_time = 0
        min_time = 0
        count = 0
        for i in trans:
            if i.time >= max_time:
                max_time = i.time

        if max_time - hours >= 0:
            min_time = max_time - hours

        for t in trans:
            if t.time >= min_time and t.time <= max_time and t.type == 'Withdraw':
                count+=1
    
        if count > max_withdrawals:
            return True
        else:
            return False


a = BankAccount('Ahmad',10000)
a.withdraw(1001,2)
a.deposit(4000,3)
a.deposit(3000,7)
a.withdraw(4000,3)
a.withdraw(5000,27)
a.withdraw(5000,27)
a.withdraw(700,27)

print(FraudDetector.check_withdrawal_limit(a))
print(FraudDetector.check_frequency(a,2))


    