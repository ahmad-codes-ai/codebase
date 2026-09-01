'''
5. Restaurant Table Reservation System with Waitlist
Context: A restaurant has tables of varying sizes (2-seater, 4-seater, etc.). Customers can make reservations for a specific date and time. If no table is available, they are placed on a waitlist. When a reservation is cancelled, the system automatically assigns the table to the first waitlisted party whose group size fits.
Task: Create classes:
Table: with attributes table_number, capacity (max guests), is_available (private boolean). Methods: reserve(), free().

Reservation: with attributes customer_name, guest_count, datetime, table (reference to Table).

Restaurant: with private attributes:

__tables (list of Table)
__reservations (list of Reservation)
__waitlist (list of (customer_name, guest_count, datetime) – ordered) Methods:
add_table(table).
make_reservation(customer, guests, datetime) – find first available table with capacity >= guests; if found, create Reservation, mark table busy, add to reservations; else add to waitlist.
cancel_reservation(customer, datetime) – find and remove the reservation, free the table, then process waitlist: assign first waiting group that fits a free table.
get_waitlist() – return waitlist.
Static method: find_available_table(tables, guests) – returns table or None.

Class variable: MIN_TABLE_CAPACITY maybe not needed.

Sample Usage:
rest = Restaurant()
rest.add_table(Table(1, 2))
rest.add_table(Table(2, 4))
rest.make_reservation("Alice", 2, "2026-07-15 19:00")  # Table 1 assigned
rest.make_reservation("Bob", 4, "2026-07-15 19:00")    # Table 2 assigned
rest.make_reservation("Charlie", 3, "2026-07-15 19:00") # no table, waitlist
rest.cancel_reservation("Bob", "2026-07-15 19:00")      # frees Table 2, assigns to Charlie
print(rest.get_waitlist())  # should be empty
'''

class Table:
    def __init__(self,no,cap):
        self.no = no
        self.cap = cap
        self.__is_available = True

    def reserve(self):
        if self.__is_available:
            self.__is_available = False
            return True
        else:
            return False

    def free(self):
        if self.__is_available:
            return "Table already free"
        else:
            self.__is_available = True
            return "Table is free now"

    def status(self):
        if self.__is_available:
            return True
        else:
            return False


class Reservation:
    def __init__(self,name,count,date,table):
        self.name = name
        self.count = count
        self.date = date
        self.table = table

class Restaurant:
    def __init__(self):
        self.__reservations = []
        self.__tables = []
        self.__waitlist = []

    def add_table(self,table):
        if table not in self.__tables:
            self.__tables.append(table)
            return True
        else:
            return False

    def make_reservation(self,customer, guests, datetime):
        found = False
        for i in self.__tables:
            if i.status() and i.cap >= guests:
                r = Reservation(customer,guests,datetime,i)
                i.reserve()
                self.__reservations.append(r)
                found = True
                return found
        
        self.__waitlist.append([customer,guests,datetime])
        return False

    def cancel_reservation(self,customer,datetime):
        to_remove = None
        found = False
        for i in self.__reservations:
            if i.name.lower().strip() == customer.lower().strip() and i.date.lower().strip() == datetime.lower().strip():
                to_remove = i
                table = i.table
                table.free()
                found = True
        if found:
            self.__reservations.remove(to_remove)
            for waiting in self.__waitlist:
                if table.cap >= waiting[1] and datetime.lower().strip() == waiting[-1].lower().strip():
                    r = Reservation(waiting[0],waiting[1],waiting[2],table=table)
                    table.reserve()
                    self.__reservations.append(r)
                    self.__waitlist.remove(waiting)
                    return "Removed and gived"
            return "Removed"
        else:
            return "Not removed"

    def get_waitlist(self):
        data = [(i[0],i[1],i[2]) for i in self.__waitlist]
        return data 
            
    @staticmethod
    def find_available_table(tables, guests):
        for i in tables:
          if i.cap >= guests:
              return i
        return None



rest = Restaurant()
rest.add_table(Table(1, 2))
rest.add_table(Table(2, 4))
print(rest.make_reservation("Alice", 2, "2026-07-15 19:00"))
print(rest.make_reservation("Bob", 4, "2026-07-15 19:00"))
print(rest.make_reservation("Charlie", 3, "2026-07-15 19:00"))
print(rest.cancel_reservation("Bob", "2026-07-15 19:00"))
print(rest.get_waitlist())
print(rest.cancel_reservation("Zebra", "2026-07-15 19:00"))
print(rest.make_reservation("Dave", 2, "2026-07-16 20:00"))
print(rest.cancel_reservation("Alice", "2026-07-15 19:00"))