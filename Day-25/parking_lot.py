class Car:
    def __init__(self,licence,name):
        self.licence = licence
        self.name = name


class ParkingSpot:
    def __init__(self,no,occupied=False):
        self.no = no
        self.__occupied = occupied

    def get_status(self):
        if self.__occupied:
            return True
        else:
            return False
        
    def change_status(self,status):
        self.__occupied = status

class Parkinglot:
    def __init__(self):
        self.spots = []
        self.car = None

    def add_spot(self,spot):
        self.spots.append(spot)
        return "Spot added"
    
    def park_car(self,car):
        if len(self.spots) > 0:
            for i in self.spots:
                if i.get_status():
                    return "No spot left all occupied"
                else:
                    i.change_status(True)
                    i.car = car
                    return "Car parked successfuly"
        else:
            return "No spot is in lot"
        
    
