'''
Problem 13: Hotel Room Booking
Context: A hotel needs to manage room reservations.

Task: Create a Room class with:

Attributes: room_number, price_per_night, is_booked (private).
Methods:
book() – mark booked if free; else print "Occupied".
cancel() – mark free.
get_status() – return "Booked" or "Available".
Create rooms, book/cancel.
'''


class Room:

  def __init__(self,room_no,price_per_night,is_booked=False):
    self.room = room_no
    self.price = price_per_night
    self.__booked = is_booked

  def book(self):
    if self.__booked:
      print("Not available")
    else:
      print("Room is booked by you")
      self.__booked = True

  def cancel(self):
    self.__booked = False
    print("Room is free now")

  def get_status(self):
    if self.__booked:
      return "Booked"
    else:
      return "Available"

r1 = Room(101,100)
r2 = Room(101,90)
r1.book()
print(r2.get_status())
r1.book()
