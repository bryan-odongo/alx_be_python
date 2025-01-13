class Book:
    def __init__(self, title, author):
        """Initialize a book with title, author, and set it as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is available.

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Return the availability of the book."""
        return self._is_checked_out

    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize the library with an empty collection of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f"Checked out: {book}")
                return
        print(f"Book '{title}' is either not available or already checked out.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f"Returned: {book}")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """List all books that are available for check-out."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No available books.")

