'''
10. Customer Loyalty Program with Tier Levels
Context: A retail store rewards customers with points and tiers.

Task: Create a Customer class with:

Private attributes: __name, __points (int).

Attributes: tier (calculated from points: 0-100: Bronze, 101-500: Silver, 501+: Gold).

Methods:

add_points(amount) – adds points, updates tier automatically.

redeem_points(points_to_redeem) – if sufficient points, deduct and return discount value (100 points = $1 discount).

Static method: points_to_discount(points) – returns discount amount (points/100).

Class variable: TIER_THRESHOLDS = {"Bronze": 0, "Silver": 101, "Gold": 501}.

Sample Usage:

cust = Customer("John")
cust.add_points(200)
print(cust.tier)  # Silver
discount = cust.redeem_points(150)  # redeem 150 points => $1.5 discount
print(cust._Customer__points)  # 50 (private attribute access not recommended)

'''


class Customer:

    TIER_THRESHOLDS = {"Bronze": 0, "Silver": 101, "Gold": 501}

    def __init__(self,name):
        self.name = name
        self.__points = 0
        self.tier = 'Bronze'

    def set_tier(self):
        if self.__points > 501:
            self.tier = 'Gold'
        elif self.__points > 101:
            self.tier = 'Silver'
        else:
            self.tier = 'Bronze'

    def add_points(self,amount):
        self.__points+=amount
        self.set_tier()
        return "Points added successfully"
    
    def redeem_points(self,amount):
        if self.__points >= amount:
            dis = amount / 100.0
            self.__points-=amount
            self.set_tier()
            return dis
        else:
            return "Insufficent points"
        
    @staticmethod
    def points_to_discount(points):
        return points/100.0
    
cust = Customer("John")
cust.add_points(200)
print(cust.tier)  # Silver
discount = cust.redeem_points(150)  # redeem 150 points => $1.5 discount
print(discount)
print(cust._Customer__points)  # 50 (private attribute access not recommended)