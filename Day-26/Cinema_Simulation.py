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



