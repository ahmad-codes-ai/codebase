'''
Easy Problem 4 – Movie Theater Seat Booking
Context A small cinema has a single hall with seats arranged in rows and columns.

Task Create a Seat class with:

Private __is_booked (bool).
Methods: book() – marks booked (if free), cancel() – frees seat.
Getter is_booked().
Create a Theater class that:

Has a 2D list of Seat objects (initialised with rows and cols).
Methods: book_seat(row, col) – books if free, else print "Occupied".
available_seats() – returns count of free seats.
display_seats() – prints a grid (e.g., [ ] for free, [X] for booked).
Sample Usage

theater = Theater(3, 4)  # 3 rows, 4 cols
theater.book_seat(1, 1)   # book row 1, col 1
print(theater.available_seats())  # 11
theater.display_seats()   # shows grid
'''


class Seat:
  def __init__(self,row,col):
    self.row = row
    self.col = col
    self.__isbooked = False

  def book(self):
    if self.__isbooked:
      return False
    else:
      self.__isbooked = True
      return True

  def cancel(self):
    self.__isbooked = False

  def is_booked(self):
    if self.__isbooked:
      return True
    return False


class Theater:
  def __init__(self,row,col):
    self.row = row
    self.col = col
    self.seats = []
    self.booked_grid = []
    for i in range(1,self.row+1):
      for j in range(1,self.col+1):
        seat = Seat(i,j)
        self.seats.append(seat)

  def book_seat(self,r,c):
    result = False
    for i in self.seats:
      if i.row == r and i.col == c:
        result = i.book()
    if result:
      self.booked_grid.append([r,c])
      return True
    print("Occupied")
    return False

  def available_seats(self):
    count = 0
    for i in self.seats:
      if not i.is_booked():
        count+=1
    return count

  def display_seats(self):
    for i in range(1,self.row+1):
      for j in range(1,self.col+1):
        print('[ ]' if [i,j] not in self.booked_grid else '[X]',end=' ')
      print()


    


theater = Theater(3, 4)  # 3 rows, 4 cols
theater.book_seat(1, 1)   # book row 1, col 1
print(theater.available_seats())  # 11 
theater.book_seat(1,2)
theater.display_seats() # shows grid
