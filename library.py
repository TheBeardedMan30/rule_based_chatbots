
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def checkout(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"The book '{self.title}' by {self.author} has been checked out in your name.")
        else:
            print(f"Sorry, the book is already checked out by someone else.")

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print("The book is already in the library.")

# Creating instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")

# Checking out and returning books
book1.checkout() # What will this print to the console?
book1.checkout() # What about this one?
book1.return_book() # What will this print?
book2.checkout()