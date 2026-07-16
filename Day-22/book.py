'''
Problem 5: Library Book Lending
Context: A library needs to track book availability.

Task: Create a Book class with:

Attributes: title, author, isbn (private __isbn).
Private attribute __is_checked_out (boolean).
Methods:
check_out() – mark as checked out (if already checked out, print message).
return_book() – mark as available.
is_available() – return status.
Create a book, check out, return, and check status.
'''


class Book:
  def __init__(self,title,author,isbn):
    self.title = title
    self.author = author
    self.__isbn = isbn
    self.__is_checkout = False

  def checkout(self):
    if not self.__is_checkout:
      print("Checkout sucessfully")
      self.__is_checkout = True
    else:
      print("Book is not available already checked out")

  def return_book(self):
    if self.__is_checkout:
      print("Book returned successfully")
    else:
      print("You didnt took a book so no book to return")

  def is_available(self):
    if self.__is_checkout:
      print("This book is not available")
    else:
      print("The book is available")

b1 = Book('Atmoic Habits','XYZ',1001)
b1.is_available()
b1.checkout()
b1.is_available()
b1.return_book()
b1.is_available()