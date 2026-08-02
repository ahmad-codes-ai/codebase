'''
Medium Problem 7 – Hotel with Dynamic Pricing and Reviews
Context A hotel chain has multiple rooms. Room prices vary by season (peak/off‑peak) and occupancy. Guests can leave reviews, and the hotel calculates an average rating.

Task Create the following classes:

Room

Attributes: room_number, room_type (single/double/suite), base_rate.
Private: __is_occupied.
Methods: check_in(), check_out().
get_price(season_factor) – returns base_rate * season_factor.
Guest

Private: __name, __reviews (list of Review objects).
Methods: leave_review(room, rating, comment).
Review

Attributes: guest, room, rating (1‑5), comment, date.
Override __str__.
Hotel

Manages __rooms (list) and __reviews (list).
Methods: add_room(room), get_available_rooms().
get_average_rating() – average of all reviews.
get_room_reviews(room_number).
Class variable: PEAK_SEASON_FACTOR = 1.5, OFF_SEASON_FACTOR = 0.8.
Static method: is_peak_season(month) – months 6‑8 are peak.
Additional

Use @property for occupancy status.
Override __len__ for Hotel to return total rooms.
Sample Usage

hotel = Hotel()
hotel.add_room(Room(101, "double", 100))
guest = Guest("Alice")
room = hotel.get_available_rooms()[0]
room.check_in()
guest.leave_review(room, 5, "Great!")
print(hotel.get_average_rating())  # 5.0
'''


class Room:
  def __init__(self,room_no,room_type,base_rate,occ=False):
    self.room_no = room_no
    self.room_type = room_type
    self.base_rate = base_rate
    self.__is_occupied = occ
    self.hotel = None


  def set_hotel(self,hotel):
    self.hotel = hotel

  def check_in(self):
    if not self.__is_occupied:
      self.__is_occupied = True
      return True
    return False

  def get_status(self):
    return self.__is_occupied

  def check_out(self):
    self.__is_occupied = False
  
  def get_price(self,season_factor):
    return self.base_rate * season_factor

  
class Guest:
  def __init__(self,name):
    self.__name = name
    self.__reviews = []

  def leave_review(self, room, rating, comment,date='12-4-2026'):
    r = Review(self.__name,room,rating,comment,date)
    hotel = room.hotel 
    hotel.add_review(r)
    self.__reviews.append(r)
    return None


class Review:
  def __init__(self,guest,room,rating,comment,date):
    self.guest = guest
    self.room = room
    self.rating = rating
    self.comment = comment
    self.date = date

  def __str__(self):
    return f"Guest: {self.guest} \n Room: {self.room.room_no} \n Rating: {self.rating}"


class Hotel:

  PEAK_SEASON_FACTOR = 1.5
  OFF_SEASON_FACTOR = 0.8

  @staticmethod
  def is_peak_season(month):
    if month in [6,7,8]:
      return True
    return False

  def __init__(self):
    self.__rooms = []
    self.__reviews = []

  def add_room(self,room):
    if room not in self.__rooms:
      room.set_hotel(self)
      self.__rooms.append(room)
      return True
    return False

  def add_review(self,rev):
    self.__reviews.append(rev)


  def __len__(self):
    return len(self.__rooms)

  def get_available_rooms(self):
    aval = []
    for room in self.__rooms:
      if not room.get_status():
        aval.append(room)
    return aval

  def get_average_rating(self):
    s = 0
    for i in self.__reviews:
      s+=i.rating
    total = len(self.__reviews)
    print(s)
    print(total)
    avg = s/total
    return avg

  def get_room_reviews(self, room_number):
    result = []
    for review in self.__reviews:
      if review.room.room_no == room_number:
        result.append(review)
    return result

  
