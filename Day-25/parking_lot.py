'''
8. Parking Lot System
Context: A parking garage needs to manage spots.

Task: Create three classes:

Car with attributes: license_plate, owner_name.

ParkingSpot with attributes: spot_number, is_occupied (private), car (reference to Car if occupied).

Methods: park(car), leave().

ParkingLot with attributes: spots (list of ParkingSpot).

Methods: find_available_spot() – returns spot number or None.

park_car(car) – parks in first available spot.

remove_car(license_plate) – removes car by plate.
'''



class Car:
    def __init__(self,licence,name):
        self.licence = licence
        self.name = name


class ParkingSpot:
    def __init__(self,no,occupied=False):
        self.no = no
        self.__occupied = occupied
        self.car = None

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
        
    def remove_car(self,l):
        for i in self.spots:
            if i.get_status():
                c = i.car
                if c.licence == l:
                    i.change_status(False)
                    i.car = None
                    return "Successfully removed"
                
car = Car(12,'Ahmad')
car2 = Car(13,'Ali')

space = ParkingSpot(1)
lot = Parkinglot()
print(lot.add_spot(space))
print(lot.park_car(car2))

print(lot.park_car(car))
print(lot.remove_car(13))
print(lot.park_car(car))
