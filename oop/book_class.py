# book_class.py

class Book:
    """
    Represents a book with a title, author, and publication year.
    Demonstrates the use of __init__, __del__, __str__, and __repr__ magic methods.
    """
    def __init__(self, title, author, year):
        """
        Constructor: Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        # print(f"Book '{self.title}' created.") # Optional: for verbose creation feedback

    def __del__(self):
        """
        Destructor: Prints a message when the Book object is about to be deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String Representation: Returns a user-friendly string for the Book object.
        Used by print() and str().
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official Representation: Returns a string that would recreate the Book instance.
        Used by repr() and in interactive shells.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
