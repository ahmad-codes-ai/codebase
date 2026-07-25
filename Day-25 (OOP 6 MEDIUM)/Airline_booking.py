'''
9. Airline Ticket Booking System
Context: An airline needs to manage flight bookings.

Task: Create a Flight class with:

Attributes: flight_number, capacity, passengers (dict: passenger_name -> seat_number).

Methods:

book_seat(passenger_name) – if capacity not reached, assign next available seat number (starting from 1), add to passengers.

cancel_booking(passenger_name) – remove passenger, free seat.

get_passenger_list() – returns list of passenger names.

available_seats() – returns remaining seats.

Class variable: total_flights (incremented on creation).

Class method: get_total_flights() – returns total enrolled across all courses.

Sample Usage:

f1 = Flight("PK101", 2)
f1.book_seat("Ali")  # seat 1
f1.book_seat("Sara") # seat 2
f1.book_seat("John") # full
print(f1.get_passenger_list())  # ["Ali", "Sara"]
'''

class Flight:

    total_flights = 0

    def get_total_flights():
        return Flight.total_flights

    def __init__(self,name,cap):
        self.name = name
        self.capacity = cap
        self.seats_available = [i for i in range(1,self.capacity + 1)]
        self.passengers = {}
        Flight.total_flights+=1
    
    def book_seat(self,pname):
        if pname not in self.passengers:
            if len(self.seats_available) > 0:
                seat = self.seats_available.pop(0)
                self.passengers[pname] = seat
                return f"Seat No: {seat} has been assigned to {pname}"
            else:
                return "No seats available"
        else:
            return "Seat with this name already exist"
        
    
    def cancel_booking(self,pname):
        if pname in self.passengers:
            sb = self.passengers.pop(pname)
            self.seats_available.append(sb)
            return f"The booking by {pname} for seat no: {sb} has been canceled"
        else:
            return "No booking found for this this name"
        
    def get_passenger_list(self):
        return self.passengers

    def available_seats(self):
        return self.available_seats
    
f1 = Flight("PK101", 2)
print(f1.book_seat("Ali"))  # seat 1
print(f1.book_seat("Sara")) # seat 2
f1.book_seat("John") # full
print(f1.get_passenger_list())  