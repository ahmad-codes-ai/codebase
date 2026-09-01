class Book:

    def __init__(self,author,name,pages,checkout=False):
        self.author = author
        self.name = name
        self.pages = pages
        self.__checkout = checkout

    def take(self):
        if self.__checkout:
            print("Book not available")
        else:
            print(f"{self.name} is given to you")
            self.__checkout = True

    def return_book(self):
        print(f"The book {self.name} has been returned successfuly")
        self.__checkout = False

    def show(self):
        print(f"Author: {self.author} \n Name: {self.name} \n Pages: {self.pages}")

    def status(self):
        if self.__checkout:
            return "Not available"
        else:
            return "Available"
        

class Library:

    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,n):
        found = False
        for book in self.books:
            if book.name.lower().strip() == n.lower().strip():
                self.books.remove(book)
                found = True
        if found:
            print("Book removed")
        else:
            print("Book not found")

    def show_books(self):
        for i in self.books:
            print(f"Author: {i.author}, Name: {i.name},  Pages: {i.pages}")



b1 = Book('Eric','Python crash course',120)
b2 = Book('ABC','Python',300)
b3 = Book('XYZ','Data Science',500)

tech_lib = Library('Tech Lib')

tech_lib.add_book(b1)
tech_lib.add_book(b2)
tech_lib.add_book(b3)

b1.take()
print(b1.status())