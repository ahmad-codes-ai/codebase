

def book_seats(self,row_col_list, customer):  # -> ([(1,1), (1,2)], "Alice")
    booked = []
    for row,col in row_col_list:
        seat = self.hall.get_seat(row,col)
        if seat is None:
            for i in booked:
                i.cancel()
            return None
    
        else:
            if not seat.status():
               seat.book()
               booked.append(seat)
    self.customers[customer] = booked   # -> Seat Objects stored in a list as values
    return booked  # -> These are seat objects