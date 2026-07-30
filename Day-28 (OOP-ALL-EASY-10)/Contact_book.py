'''
Easy Problem 6 – Contact Book
Context A simple address book to store contacts.

Task Create a Contact class with:

Private attributes: __name, __phone, __email.
Getters and setters for phone (with validation: must be digits only).
Override __str__.
Create an AddressBook class that:

Has a list of Contact objects.
Methods: add_contact(contact), remove_contact(name).
search(name) – returns contact if found, else None.
Sample Usage

book = AddressBook()
book.add_contact(Contact("Alice", "1234567890", "alice@x.com"))
book.add_contact(Contact("Bob", "0987654321", "bob@x.com"))
print(book.search("Alice"))  # shows Alice's details
book.remove_contact("Bob")
'''


class Contact:
  def __init__(self,name,phone,email):
    self.__name = name
    self.__phone = phone
    self.__email = email

  def get_phone(self):
    return self.__phone

  def get_name(self):
    return self.__name

  def set_phone_number(self,no):
    if no.isdigit():
      self.__phone = no
      return True
    return False

  def __str__(self):
    s = f"Name: {self.__name}, Phone: {self.__phone}, Email: {self.__email}"
    return s


class AddressBook:
  def __init__(self):
    self.contacts = []
  
  def add_contact(self,con):
    if con not in self.contacts:
      self.contacts.append(con)
      return True
    return False

  def remove_contact(self,name):
    for i in self.contacts:
      if i.get_name() == name:
        self.contacts.remove(i)
        return True
    return False

  def search(self,name):
    for i in self.contacts:
      if i.get_name() == name:
        return i
    return None

book = AddressBook()
book.add_contact(Contact("Alice", "1234567890", "alice@x.com"))
book.add_contact(Contact("Bob", "0987654321", "bob@x.com"))
print(book.search("Alice"))  # shows Alice's details
book.remove_contact("Bob")
  