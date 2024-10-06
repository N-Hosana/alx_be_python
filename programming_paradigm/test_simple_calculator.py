# Define the Book class
class Book:
    """A class representing a book with a title and author."""
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Returns whether the book is available to check out."""
        return not self._is_checked_out

# Define the Library class
class Library:
    """A class to represent a collection of books in a library."""
    
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book from the library by title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                else:
                    print(f"Sorry, {title} is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book to the library by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                else:
                    print(f"{title} was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books at the moment.")
