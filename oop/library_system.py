# library_system.py

class Book:
    """
    Base class for all books in the library system.
    """
    def __init__(self, title, author):
        """
        Initializes a Book instance with a title and author.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the Book object for display.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance, calling the base Book constructor
        and adding a file_size attribute.

        Args:
            title (str): The title of the e-book.
            author (str): The author of the e-book.
            file_size (int): The file size of the e-book in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns a string representation of the EBook object for display,
        including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a physical print book, inheriting from Book.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance, calling the base Book constructor
        and adding a page_count attribute.

        Args:
            title (str): The title of the print book.
            author (str): The author of the print book.
            page_count (int): The number of pages in the print book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns a string representation of the PrintBook object for display,
        including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library that manages a collection of various book types.
    Demonstrates composition.
    """
    def __init__(self):
        """
        Initializes a Library instance with an empty list to store books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book (or EBook/PrintBook) instance to the library's collection.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        if isinstance(book, Book):
            self.books.append(book)
            # print(f"Added '{book.title}' to the library.") # Optional: for verbose feedback
        else:
            print("Error: Only Book instances (or derived classes) can be added to the library.")

    def list_books(self):
        """
        Prints the details of each book currently in the library.
        """
        if not self.books:
            print("The library is currently empty.")
        else:
            for book in self.books:
                print(book) # This calls the __str__ method of each book object
