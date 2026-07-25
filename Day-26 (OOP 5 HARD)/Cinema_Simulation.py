'''
4. Movie Theater Booking System with Showtimes
Context: A multiplex cinema has multiple screens (halls). Each hall has a fixed number of seats arranged in rows and columns. Customers can book seats for a specific showtime. The system must prevent double-booking and allow cancellations. Also, it should provide a real-time seat map.
Task: Create classes:
Seat: with attributes row, number, is_booked (private). Methods: book(), cancel().

Hall: with attributes name, rows, columns, seats (2D list of Seat objects). Methods:

get_seat(row, col) returns Seat.
get_available_seats() returns list of (row, col) tuples.
Showtime: with attributes movie_title, hall, start_time (string). Methods:

book_seats(row_col_list, customer) – attempts to book multiple seats; if any unavailable, rollback? (For simplicity, book individually and return list of booked seats or None if any fail).
cancel_booking(row_col_list, customer) – frees seats.
Cinema: manages multiple Hall objects and Showtime objects. Methods to add hall, add showtime, search shows by movie.

Static method: validate_seat(row, col, hall) – checks bounds.

Class variable: MAX_CANCELLATIONS_PER_CUSTOMER = 2 – maybe use it per show.

Sample Usage:
hall = Hall("Screen 1", 5, 8)
show = Showtime("Avengers", hall, "18:00")
booking = show.book_seats([(1,1), (1,2)], "Alice")  # returns list of seats
show.cancel_booking([(1,1)], "Alice")  # frees one seat
'''


class Seat:
    def __init__(self,row,number):
        self.row = row
        self.col = number
        self.__isbooked = False

    def book(self):
        if not self.__isbooked:
            self.__isbooked = True
            return 'Seat booked'
        else:
            return 'Seat not available'

    def cancel(self):
        if self.__isbooked:
            self.__isbooked = False
            return "Seat canceleed"
        else:
            return "Seat is already free"

    def status(self):
        return self.__isbooked

class Hall:
    def __init__(self,name,row,col):
        self.name = name
        self.row = row
        self.col = col
        self.seats = []
        self.make_seats()

    def make_seats(self):
        for i in range(1,self.row+1):
            for j in range(1,self.col+1):
                t = Seat(i,j)
                self.seats.append(t)

    def get_seat(self,r,c):
        seat = (r,c)
        for i in self.seats:
            s = (i.row,i.col)
            if s == seat:
                return i
        return None

    def get_available_seats(self):
        available = []
        for i in self.seats:
            if not i.status():
                available.append((i.row,i.col))
        return available

class ShowTime:
    def __init__(self,title,hall,time):  # -> hall object 1
        self.title = title
        self.hall = hall
        self.time = time
        self.customers = {}

    def book_seats(self,row_col_list, customer):  # -> ([(1,1), (1,2)], "Alice")
        booked = []
        all_avail = []
        available = self.hall.get_available_seats()
        for row,col in row_col_list:
            s = (row,col)
            if s in available:
                all_avail.append(s)
            else:
                return None
       
        for i,j in all_avail:
            seat = self.hall.get_seat(i,j)
            seat.book()
            booked.append(seat)
        if customer not in self.customers:
            self.customers[customer] = booked
        else:
            for i in booked:
                self.customers[customer].append(i)
        return [(i.row,i.col) for i in booked]
        
        
    def cancel_booking(self,row_col_list, customer):
        if customer in self.customers:
            cancel_seats = []
            for row,col in row_col_list:
                seat = self.hall.get_seat(row,col)
                if seat is not None and seat in self.customers[customer]:
                    seat.cancel()
                    cancel_seats.append(seat)
                else:
                    return False
            
            updated_seats = []
            for i in self.customers[customer]:
                if i not in cancel_seats:
                    updated_seats.append(i)
            self.customers[customer] = updated_seats
            return True
        else:
            return False
            


class Cinema:
    def __init__(self,name):
        self.name = name
        self.halls = []
        self.shows = []

    def add_hall(self,hall):
        if hall not in self.halls:
            self.halls.append(hall)
            return "Hall added"
        else:
            return "Hall already exist in cinema"

    def add_show(self,show):
        if show not in self.shows:
            self.shows.append(show)
            return "Show added"
        else:
            return "Show already exist"  

    def search_shows_by_movie(self, movie_title):
        occurance = []
        for i in self.shows:
            if i.title.lower().strip() == movie_title.lower().strip():
                occurance.append((movie_title,i.time))
        return occurance

    @staticmethod
    def validate_seat(row, col, hall):
        if hall.get_seat(row,col) is not None:
            return True
        else:
            return False


cinema = Cinema("Test")
hall = Hall("A", 3, 4)
show = ShowTime("TestMovie", hall, "12:00")
cinema.add_hall(hall); cinema.add_show(show)

print(show.book_seats([(1,1),(1,2)], "Alice"))   # Expected: [(1,1),(1,2)]
print(hall.get_available_seats())                # All except (1,1),(1,2)
print(show.cancel_booking([(1,1)], "Alice"))    # Expected: True
print(Cinema.validate_seat(2, 3, hall))          # Expected: True
print(Cinema.validate_seat(5, 1, hall))          # Expected: False
print(show.book_seats([(1,2)], "Bob"))           # Expected: [(1,1)] (now free) -> The test case sample is wrong (1,1) was never canceled so it should be None
print(show.cancel_booking([(1,1),(1,2)], "Bob"))
