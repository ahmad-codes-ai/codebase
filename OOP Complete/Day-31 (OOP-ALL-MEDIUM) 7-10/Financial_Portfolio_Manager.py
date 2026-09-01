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

class MarketData:
   prices =  {
    "AAPL": 150.0,
    "GOOGL": 2800.0,   
    "BTC": 30000.0,
    "ETH": 2000.0
}
   
   @staticmethod
   def get_price(symbol,prices=prices):
    for i in prices:
      if i == symbol:
        return prices[i]
    return 0.0

class Asset:
  def __init__(self,symbol,quan,pur_price):
    self.symbol = symbol
    self.quantity = quan
    self.__purchase_price = pur_price

  def get_current_price(self):
    return MarketData.get_price(self.symbol)

  def get_purchase_price(self):
    return self.__purchase_price

  def current_value(self):
    return self.quantity * self.get_current_price()
    

  def profit_loss(self):
    return (self.get_current_price() - self.__purchase_price) * self.quantity

class Stock(Asset):
  def get_current_price(self):
    return MarketData.get_price(self.symbol)

class Crypto(Asset):
  def __init__(self,symbol,quan,pur_price,market_cap):
    super().__init__(symbol,quan,pur_price)
    self.market_cap = market_cap

  def get_current_price(self):
    return MarketData.get_price(self.symbol)

class Bond(Asset):
  def __init__(self,symbol,quan,pur_price,coupon):
    super().__init__(symbol,quan,pur_price)
    self.coupon_rate = coupon 

  def get_current_price(self):
    return self.get_purchase_price() * (1 + self.coupon_rate)

class Portfolio:
  def __init__(self):
    self.__assets = []

  def add_asset(self,asset):
    if asset not in self.__assets:
      self.__assets.append(asset)
      return True
    return False

  def total_value(self):
    total = 0
    for asset in self.__assets:
      total+=asset.current_value()
    return total

  def total_profit_loss(self):
    total = 0
    for asset in self.__assets:
      p = asset.profit_loss()
      if p > 0:
        total+=p
      else:
        total-=p 
    return total

  def get_allocation(self):
    d = {'stock':0,'crypto':0,'bond':0}
    total = 0
    for asset in self.__assets:
      val = asset.current_value()
      total+=val
      if isinstance(asset,Stock):
        d['stock']+=val
      elif isinstance(asset,Crypto):
        d['crypto']+=val
      elif isinstance(asset,Bond):
        d['bond']+=val

    allocation = {'stock': (d['stock']/total)*100,
                  'crypto': (d['crypto']/total)*100,
                  'bond': (d['bond']/total)*100}  
    return allocation
  
  def __add__(self,others):
    new = Portfolio()

    new._Portfolio__assets = self._Portfolio__assets + others._Portfolio__assets
    return new 
  
stock = Stock("AAPL", 10, 140)
bond = Bond("US10Y", 5, 95, 0.03)
portfolio = Portfolio()
portfolio.add_asset(stock)
portfolio.add_asset(bond)
print(portfolio.total_value())  # 10*150 + 5*100 (approx) = 2000
print(portfolio.get_allocation())