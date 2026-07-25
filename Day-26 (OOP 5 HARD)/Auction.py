'''
2. Online Auction System
Context: An auction platform allows users to list items and place bids. Each item has a starting price, a reserve price, and a bid history. Bids must be higher than the current highest bid by a minimum increment (e.g., $1). The system must track active items and notify winners when the auction ends (simulate with a method call).
Task: Create classes:
Bid: with attributes bidder_name, amount, timestamp.

AuctionItem: with private attributes __current_bid (float), __highest_bidder, __bid_history (list of Bid). Public attributes: item_name, starting_price, reserve_price, minimum_increment (default 1.0). Methods:

place_bid(bidder, amount) – if amount > current_bid + min_increment, accept bid, update highest.
get_current_bid(), get_highest_bidder().
close_auction() – returns the winning Bid or None if reserve not met.
AuctionHouse: manages multiple items, has methods add_item(item), get_active_items(), close_all().

Static method: is_valid_bid(amount, current_bid, min_increment) – checks if bid is valid.

Class variable: DEFAULT_INCREMENT = 1.0.

Sample Usage:
house = AuctionHouse()
item = AuctionItem("Vintage Car", 1000, 1500, 50)  # min increment 50
house.add_item(item)
item.place_bid("John", 1050)  # valid
item.place_bid("Alice", 1100) # valid
winner = item.close_auction() # should return Alice's bid if >= reserve
print(winner.bidder_name)  # Alice
'''

class Bids:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount


class AuctionItem:
    def __init__(self,name,sp,rp,mi=1.0):
        self.name = name
        self.start_price = sp
        self.reserve_price = rp
        self.min_increment = mi 
        self.status = True
        self.__current_bid = 0
        self.__highest_bidder = None
        self.__bid_history = []

    def place_bid(self,bidder,amount):
        bid = Bids(bidder,amount=amount)
        if bid.amount > self.__current_bid + self.min_increment:
            self.__highest_bidder = bid
            self.__current_bid = bid.amount
            self.__bid_history.append(bid)
            return "Bid placed successfully"
        else:
            return "Bid criteria not met"

    def get_current_bid(self):
        return self.__current_bid

    def get_highest_bidder(self):
        return self.__highest_bidder

    def close_auction(self):
        self.status = False
        if self.__current_bid >= self.reserve_price:
            return self.__highest_bidder
        else:
            self.__highest_bidder.name= None
            return self.__highest_bidder
        

class AuctionHouse:

    DEFAULT_INCREMENT = 1.0

    def __init__(self):
        self.items = []

    def add_item(self,item):
        if item not in self.items:
            self.items.append(item)
            return "Item added successfully"
        else:
            return "Item already exist"

    def get_active_items(self):
        active = []
        for i in self.items:
            if i.status:
                active.append(i)
        return active

    def close_all(self):
        for i in self.items:
            i.status = False

    @staticmethod
    def is_valid_bid(amount, current_bid, min_increment=None):
        if min_increment is None:
            min_increment = AuctionHouse.DEFAULT_INCREMENT
        if amount > current_bid + min_increment:
            return True
        else:
            return False

house = AuctionHouse()
item = AuctionItem("Vintage Car", 1000, 1500, 50)  # min increment 50
house.add_item(item)
item.place_bid("John", 1050)  # valid
item.place_bid("Alice", 1100) # valid
winner = item.close_auction() # should return Alice's bid if >= reserve
print(winner.name)  # Alice

