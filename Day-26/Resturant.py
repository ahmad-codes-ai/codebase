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
                if table.cap >= waiting[1]:
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
print(rest.make_reservation("Alice", 2, "2026-07-15 19:00"))  # Table 1 assigned
print(rest.make_reservation("Bob", 4, "2026-07-15 19:00"))    # Table 2 assigned
print(rest.make_reservation("Charlie", 3, "2026-07-15 19:00")) # no table, waitlist
print(rest.cancel_reservation("Bob", "2026-07-15 19:00"))      # frees Table 2, assigns to Charlie
print(rest.get_waitlist())  # should be empty
