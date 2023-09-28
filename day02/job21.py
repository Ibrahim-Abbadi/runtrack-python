class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname

    def SePresenter(self):
        print(f"I am {self.firstname} {self.lastname}")
        
        
class Book:
    def __init__(self, title, Author):
        self.title = title 
        self.Author = Author
    def print_title(self):
        print(f"Title: {self.title}")

class Author(Person):
    def __init__(self, lastname, firstname):
        super().__init__(lastname, firstname)
        self.work = []
        
    def listerWork(self):
        print(f"Books by {self.firstname} {self.lastname}:")
        for book in self.work:
            print(f"- {book.title}")

    def writeABook(self, book_title):
        new_book = Book(book_title, self)
        self.work.append(new_book)
        print(f"{self.firstname} {self.lastname} has a new book: '{book_title}'")

author1 = Author("A", "B")
author1.listerWork()
author1.writeABook("fgjl jiùoùo")
author1.listerWork()

        