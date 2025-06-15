# library_management.py
# 
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        status = "Checked Out" if self._is_checked_out else "Available"
        return f"'{self.title}' by {self.author} ({status})"

class Library:
    """
    Manages a collection of Book objects.
    Provides methods to add, check out, return, and list books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return

        # Check if a book with the same title and author already exists
        for existing_book in self._books:
            if existing_book.title == book.title and existing_book.author == book.author:
                print(f"Book '{book.title}' by {book.author} already exists in the library.")
                return

        self._books.append(book)
        print(f"Added book: '{book.title}' by {book.author}.")

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.
        If the book is found and available, its status is updated.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book was successfully checked out, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"Checked out: '{book.title}'.")
                    return True
                else:
                    print(f"'{book.title}' is already checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def return_book(self, title):
        """
        Attempts to return a book by its title.
        If the book is found and checked out, its status is updated.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book was successfully returned, False otherwise.
        """
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"Returned: '{book.title}'.")
                    return True
                else:
                    print(f"'{book.title}' was not checked out.")
                    return False
        print(f"Book with title '{title}' not found in the library.")
        return False

    def list_available_books(self):
        """
        Lists all books in the library that are currently available (not checked out).
        """
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books:
            print("\nAvailable Books:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("\nNo books currently available in the library.")