'''
Problem 3: Document Processing
Scenario: A system processes different types of documents.

Task:

Create a base class Document with attributes title, author, and content.

Create a method get_summary() that returns the first 30 characters of the content.

Create two subclasses: PDFDocument and WordDocument.

The PDFDocument class should have an additional attribute page_count.

The WordDocument class should have an additional attribute word_count.

Override the get_summary() method in the WordDocument class to return the first 50 characters of the content.
'''


class Document:
  def __init__(self,title,author,content):
    self.title = title
    self.author = author
    self.content = content

  def get_summary(self):
    return self.content[0:30]
  
class PDFDocument(Document):
  def __init__(self,title,author,content,page):
    self.page_count = page
    super().__init__(title,author,content)

class WordDocument(Document):
  def __init__(self,title,author,content,word):
    self.word_count = word
    super().__init__(title,author,content)

  def get_summary(self):
    return self.content[0:50]