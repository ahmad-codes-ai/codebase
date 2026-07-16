'''
Problem 8: User Login System
Context: An app needs secure user authentication.

Task: Create a User class with:

Attributes: username, private __password.
Method:
login(attempt) – return True if attempt matches password, else False.
Getter/Setter for password (optional).
Create a user, test login with correct/incorrect attempts.
'''


class User:

  def __init__(self,name,pas):
    self.name = name
    self.__pas = pas

  def login(self,attempt):
    if attempt == self.__pas:
      return True
    else:
      return False

  def get_pas(self):
    print(f"Pass is : {self.__pas}")

  def change_pas(self,cp):
    if cp == self.__pas:
      np = int(input("Enter new pass: "))
      self.__pas = np
      print("Pass changed sucessfuly")

u1 = User('Ahmad',1234)
u1.login(1234)
u1.get_pas()
u1.change_pas(1234)
u1.login(3333)