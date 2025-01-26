class Book:
    def __init__(self, title, author, year):
        """Initialize the Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the Book instance is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation for the user."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return a string representation that recreates the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

