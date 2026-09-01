'''
Easy Problem 1 – Pet Adoption Center
Context A local animal shelter needs a system to manage pets available for adoption.

Task Create a Pet class with:

Private attributes: __name, __species, __age, __is_adopted (bool).
Methods: adopt() – marks as adopted (if not already), return_pet() – marks as available.
Getters for name, species, age.
Override __str__ to show pet details.
Create an AdoptionCenter class that:

Has a list of Pet objects.
Methods: add_pet(pet), get_available_pets() – returns list of available pets, adopt_pet(name) – finds by name and calls adopt().
Sample Usage

center = AdoptionCenter()
center.add_pet(Pet("Max", "Dog", 3))
center.add_pet(Pet("Whiskers", "Cat", 2))
print(center.get_available_pets())  # Max, Whiskers
center.adopt_pet("Max")
print(center.get_available_pets())  # Whiskers only
'''


class Pet:
  def __init__(self,name,spe,age,adopted=False):
    self.__name = name
    self.__species = spe
    self.__age = age
    self.__is_adopted = adopted

  def adopt(self):
    if self.__is_adopted:
      print("This pet is already adopted")
      return False
    else:
      print(f"You adopt {self.__name}")
      self.__is_adopted = True
      return True

  def return_pet(self):
    if self.__is_adopted:
      print("Pet returned successfully")
      return True
    else:
      print("You dont have this pet to return")
      return False

  def get_info(self,x):
    if x.lower() == 'name':
      return self.__name
    elif x.lower() == 'species':
      return self.__species
    elif x.lower() == 'age':
      return self.__age
    else:
      return None

  def status(self):
    if self.__is_adopted:
      return True
    else:
      return False

  def __str__(self):
    detail = [self.__name,self.__species,self.__age]
    print(detail)   

class AdoptionCenter:
  def __init__(self):
    self.pets = []

  def add_pet(self,pet):
    if pet not in self.pets:
      self.pets.append(pet)
      return True
    else:
      return False

  def get_available_pets(self):
    aval = []
    for i in self.pets:
      if not i.status():
        aval.append(i.get_info('name'))
    return aval

  def adopt_pet(self,name):
    name = name.lower().strip()
    for i in self.pets:
      if i.get_info('name').lower().strip() == name:
        i.adopt()
        return True
        
    print("Pet not available/adopted")
    return False


center = AdoptionCenter()
center.add_pet(Pet("Max", "Dog", 3))
center.add_pet(Pet("Whiskers", "Cat", 2))
print(center.get_available_pets())  # Max, Whiskers
center.adopt_pet("Max")
print(center.get_available_pets())  # Whiskers only