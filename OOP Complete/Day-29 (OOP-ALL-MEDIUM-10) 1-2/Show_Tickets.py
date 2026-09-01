'''
Medium Problem 2 – Event Ticketing with VIP Upgrades
Context An event organiser sells tickets for concerts. There are standard, VIP, and backstage tickets. Each has different perks and prices. The system must handle bulk discounts and upgrade requests.

Task Create the following classes:

Ticket (abstract)

Attributes: event_name, price, seat_number (private).
Abstract method: get_perks() – returns list of strings.
Override __str__ to show event, seat, and price.
StandardTicket (inherits Ticket) – perks: ["Entry"].

VIPTicket (inherits Ticket) – perks: ["Entry", "Fast Lane", "VIP Lounge"].

BackstageTicket (inherits Ticket) – perks: ["Entry", "Meet & Greet", "Backstage Tour"].

Order

Private: __tickets (list), __customer.
Methods: add_ticket(ticket, quantity), total_cost() – sum of price * qty.
apply_bulk_discount() – if total tickets > 5, apply 10% discount.
upgrade_ticket(seat_number, new_type) – replaces a standard ticket with VIP/Backstage (pay difference).
__add__ magic method – combine two Orders (merge tickets).
EventOrganizer

Manages available seats and pricing.
Static method: validate_seat(seat) – seat must be like "A12".
Class variable: MAX_TICKETS_PER_ORDER = 10.
Sample Usage

order = Order("Alice")
order.add_ticket(StandardTicket("Concert", 50, "A12"), 2)
order.add_ticket(VIPTicket("Concert", 120, "B5"), 1)
order.apply_bulk_discount()
order.upgrade_ticket("A12", "VIP")  # pays extra 70
print(order.total_cost())
'''

from abc import ABC, abstractmethod

class Ticket(ABC):
  def __init__(self,name,price,seat):
    self.event_name = name
    self.price = price
    self.__seat_no = seat

  def get_seat(self):
    return self.__seat_no

  def set_price(self,p):
    self.price = p

  @abstractmethod
  def get_perks(self):
    pass

  def __str__(self):
    return f"Event: {self.event_name} \n Seat: {self.__seat_no} \n Price: {self.price}"

class StandardTicket(Ticket):
  def __init__(self,name,price,seats):
    super().__init__(name,price,seats)

  def get_perks(self):
    perks = ['Entry']
    return perks

class VIPTicket(Ticket):
  def get_perks(self):
    perks = ["Entry", "Fast Lane", "VIP Lounge"]
    return perks

class BackstageTicket(Ticket):
  def get_perks(self):
    perks = ["Entry", "Meet & Greet", "Backstage Tour"]
    return perks


class Order:
  def __init__(self,customer):
    self.__tickets = []
    self.__customer = customer
    self.standard = 50
    self.vip = 120
    self.backstage = 150
    self.discount = 0

  def add_ticket(self, ticket, quantity):
    if quantity == 1:
      self.__tickets.append(ticket)
    elif quantity > 1:
      self.__tickets.append(ticket)
      for i in range(1,quantity):
        ns = f"{ticket.get_seat()}({i})"
        nt = type(ticket)(ticket.event_name,ticket.price,ns)
        self.__tickets.append(nt)


  def total_cost(self):
    total = 0
    for i in self.__tickets:
      total+=i.price
    return total - self.discount

  def apply_bulk_discount(self):
    if len(self.__tickets) > 5:
      actual = self.total_cost()
      discount = actual * 0.1
      self.discount = discount


  def upgrade_ticket(self,no,new_type):
    idx = 0
    for i in self.__tickets:
      if i.get_seat().lower().strip() == no.lower().strip():
        if new_type.lower().strip() == 'vip':
          ns = VIPTicket(i.event_name,self.vip,i.get_seat())
          self.__tickets[idx] = ns
          return True
        elif new_type.lower().strip() == 'backstage':
          ns = BackstageTicket(i.event_name,self.backstage,i.get_seat())
          self.__tickets[idx] = ns
          return True
      idx+=1
    return False

  def __add__(self,other):
    merged_name = f"{self.__customer} & {other.__customer}"
    new_order = Order(merged_name)
    new_order.__tickets = self.__tickets + other.__tickets
    return new_order

  def show_tickets(self):
    for i in self.__tickets:
      print(i)




order = Order("Alice")
order.add_ticket(StandardTicket("Concert", 50, "A12"), 2)
order.add_ticket(VIPTicket("Concert", 120, "B5"), 1)
order.apply_bulk_discount()
order.upgrade_ticket("A12", "VIP")  # pays extra 70
print(order.total_cost())
order.show_tickets()







