'''
Problem 7: Library Collection Manager
Context: A librarian wants to manage multiple books.

Task: Create a Library class that:

Has a list of Book objects (from problem 5).
Methods:
add_book(book) – add a book to the collection.
remove_book(isbn) – remove by ISBN.
search_by_title(title) – return list of matching books.
Create a few books, add them, search and remove.
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

b1 = Book('Atomic Habits','James',1001)
b2 = Book('Python crash course','Eric mathews',1077)

class Library():
  counter = 0
  def __init__(self):
    self.books = [b1,b2]
  
  def show(self):
    for i in self.books:
      print(i.__dict__)

  def add_book(self,title,author,isbn):
    book = Book(title,author,isbn)
    self.books.append(book)

  def remove_book(self,isn):
    flag = False
    for i in self.books:
      if i._Book__isbn == isn:
        self.books.remove(i)
        flag = True

    if flag:
      print("Book has been removed")
    else:
      print("Book not found")

  def search(self,t):
    flag = False
    for i in self.books:
      if i.title.lower().strip() == t.lower().strip():
        print(i.__dict__)
        flag = True

    if not flag:
      print("Book not found")

p1 = Library()
p1.search('atomic habits')