'''
Medium Problem 9 – Financial Portfolio Manager
Context An investment app tracks stocks, bonds, and crypto. Each asset has a current price and quantity. The portfolio computes total value, profit/loss, and diversification.

Task Create the following classes:

Asset (abstract)

Attributes: symbol, quantity, purchase_price (private).
Abstract method: get_current_price() – returns float.
Method: current_value() – quantity * current_price.
Method: profit_loss() – (current_price - purchase_price) * quantity.
Stock (inherits Asset) – get_current_price() simulates (use a static price list).

Bond – adds coupon_rate; get_current_price() uses face value + coupon.

Crypto – adds market_cap.

Portfolio

Private: __assets (list).
Methods: add_asset(asset), total_value(), total_profit_loss().
get_allocation() – returns dict {type: percentage}.
rebalance(target_allocations) – not required to actually trade, just suggests.
MarketData (static class)

Static dictionary prices = {"AAPL": 150, "BTC": 30000, ...}.
Static method: get_price(symbol).
Additional

Override __add__ for Portfolio to merge two portfolios (sum assets).
Use @abstractmethod.
Sample Usage

stock = Stock("AAPL", 10, 140)
bond = Bond("US10Y", 5, 95, 0.03)
portfolio = Portfolio()
portfolio.add_asset(stock)
portfolio.add_asset(bond)
print(portfolio.total_value())  # 10*150 + 5*100 (approx) = 2000
print(portfolio.get_allocation())
'''


from abc import ABC, abstractmethod

class Asset(ABC):
  def __init__(self,symbol,quan,pur_price):
    self.symbol = symbol
    self.quantity = quan
    self.__purchase_price = pur_price

  @abstractmethod
  def get_current_price(self):
    pass

  def current_value(self):
    return self.quantity * self.get_current_price()

  def profit_loss(self):
    return (self.get_current_price() - self.__purchase_price) * self.quantity

class Stock(Asset):
  def get_current_price(self):
    pass

class Bond(Asset):
  def __init__(self,symbol,qun,face,coupon):
    self.coupon_rate = coupon
    self.face_value = face
    super().__init__(symbol,qun,face)

  def get_current_price(self):
    return self.face_value * (1+self.coupon_rate)

class Crypto(Asset):
  def __init__(self,symbol,quan,pur,market):
    self.market_cap = market
    super().__init__(symbol,quan,pur)

  def get_current_price(self):
    pass



