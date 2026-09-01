''' 
1. Library Management System with Fine Calculator
Context: A public library wants to automate book lending and calculate overdue fines.

Task: Create two classes:

Book with attributes: title, author, isbn (private), is_checked_out (private boolean).

LibraryMember with attributes: name, member_id, borrowed_books (list of Book objects), days_overdue (private integer per book?).

Methods:

borrow_book(book) – checks if book is available, marks it checked out, adds to borrowed list.

return_book(book) – marks book available, removes from borrowed list, and calculates fine: $0.50 per day overdue (you can store a borrow date or just use a days_borrowed parameter for simplicity). For simplicity, let return_book(book, days_borrowed) – if days_borrowed > 14 (loan period), fine = (days_borrowed - 14) * 0.50.

get_fines() – returns total outstanding fines for this member.

Sample Usage:

book1 = Book("1984", "Orwell", "123")
member = LibraryMember("Alice", "M001")
member.borrow_book(book1)
member.return_book(book1, 20)  # 6 days overdue => fine $3.00
print(member.get_fines())      # 3.0

'''

class Book:
  def __init__(self,t,a,i,check=False):
    self.title = t
    self.author = a
    self.__isbn = i
    self.checkout = check


class LibraryMember:
  def __init__(self,name,id):
    self.name = name
    self.id = id
    self.borrowed_books = []
    self.fine = 0

  def borrow_book(self,book):
    if book.checkout:
      print("The book is not available")
    else:
      print("The book is added successfully in your borrowed list")
      book.checkout = True
      self.borrowed_books.append(book)

  def apply_fines(self,days):
    if days > 14:
      ff = (days - 14) * 0.50
    else:
      ff = 0
    return ff

  def get_fines(self):
    return self.fine

  def return_book(self,book,days):
    if book in self.borrowed_books:
      print("The book has been returned successfully")
      f = self.apply_fines(days)
      self.fine+=f
      self.borrowed_books.remove(book)
      book.checkout = False
    else:
      print("You dont have this book in your list")

book1 = Book("1984", "Orwell", "123")
member = LibraryMember("Alice", "M001")
member.borrow_book(book1)
member.return_book(book1, 20)  # 6 days overdue => fine $3.00
print(member.get_fines())      # 3.0
print(book1.checkout)
print(member.borrowed_books)