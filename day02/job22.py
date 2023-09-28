class Person:
    def __init__(self, name, first_name):
        self.name = name
        self.first_name = first_name

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, name):
        self.name = name
        self.catalog = {}

    def buyBook(self, author, book_title, quantity):
        # Check if the author exists in the catalog
        if author.name in self.catalog:
            author_books = self.catalog[author.name]
        else:
            author_books = {}

        # Check if the book exists in the author's work
        if book_title in author.books:
            # Add the book to the library catalog
            if book_title in author_books:
                author_books[book_title] += quantity
            else:
                author_books[book_title] = quantity
            self.catalog[author.name] = author_books
            print(f"{quantity} copies of '{book_title}' by {author.name} added to the catalog.")
        else:
            print(f"'{book_title}' by {author.name} does not exist in the author's work.")

    def inventory(self):
        print("Library Inventory:")
        for author_name, books in self.catalog.items():
            for book_title, quantity in books.items():
                print(f"'{book_title}' by {author_name}: {quantity} copies")

    def rent(self, customer, book_title):
        if customer.name not in self.catalog:
            print(f"'{customer.name}' is not a registered")
            return

        if book_title in self.catalog[customer.name] and self.catalog[customer.name][book_title] > 0:
            customer.books.append(Book(book_title, Person(customer.name, customer.first_name)))
            self.catalog[customer.name][book_title] -= 1
            print(f"'{book_title}' rented to {customer.name}.")
        else:
            print(f"'{book_title}' is not available")

    def renderBooks(self, customer):
        for book in customer.books:
            self.buyBook(book.author, book.title, 1)

class Customer(Person):
    def __init__(self, name, first_name):
        super().__init__(name, first_name)
        self.books = []

    def inventory(self):
        print(f"Books in possession of {self.first_name} {self.name}:")
        for book in self.books:
            print(f"'{book.title}' by {book.author.name}")


# test
author1 = Person("Author1", "AUTHOR1")
author2 = Person("Author2", "AUTHOR2")

author1.books = ["Book1", "Book2"]
author2.books = ["Book3", "Book4"]

library = Library("LIBRARY")

library.buyBook(author1, "Book1", 5)
library.buyBook(author2, "Book3", 3)

customer1 = Customer("Customer1", "Jean")
customer2 = Customer("Customer2", "Philippe")

library.rent(customer1, "Book1")
library.rent(customer1, "Book2")
library.rent(customer2, "Book3")

library.inventory()
customer1.inventory()
customer2.inventory()
