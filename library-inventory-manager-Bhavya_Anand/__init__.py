import json
from pathlib import Path
import logging
import sys

# --- Task 5: Exception Handling and Logging (Global Configuration) ---
# Configure logging for the entire application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Task 1: Book Class Design ---
class Book:
    """
    Represents a book in the library inventory.
    """
    def __init__(self, title, author, isbn, status="available"):
        """
        Initializes a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            status (str): The current status of the book (available or issued).
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status # "available" or "issued"

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status.capitalize()}"

    def to_dict(self):
        """
        Converts the Book object to a dictionary for JSON serialization.
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        """
        Issues the book if it's available.
        Returns True if successful, False otherwise.
        """
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        """
        Returns the book if it's issued.
        Returns True if successful, False otherwise.
        """
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        """
        Checks if the book is available.
        Returns True if available, False otherwise.
        """
        return self.status == "available"

# --- Task 2: Inventory Manager & Task 3: File Persistence with JSON ---
class LibraryInventory:
    """
    Manages the collection of Book objects, including persistence to a JSON file.
    """
    def __init__(self, file_path="books.json"):
        """
        Initializes the LibraryInventory.
        Loads existing books from the specified JSON file or starts with an empty inventory.

        Args:
            file_path (str): The path to the JSON file for storing book data.
        """
        self.file_path = Path(file_path)
        self.books = []
        self._load_books()

    def _load_books(self):
        """
        Loads book data from the JSON file. Handles missing or corrupted files.
        """
        if not self.file_path.exists():
            logger.info(f"Book data file not found at {self.file_path}. Starting with an empty inventory.")
            return

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Reconstruct Book objects from dictionary data
                self.books = [Book(**book_data) for book_data in data]
            logger.info(f"Successfully loaded {len(self.books)} books from {self.file_path}.")
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON from {self.file_path}. File might be corrupted. Starting with an empty inventory.")
            self.books = []
        except Exception as e:
            logger.error(f"An unexpected error occurred while loading books from {self.file_path}: {e}")
            self.books = []

    def _save_books(self):
        """
        Saves the current book inventory to the JSON file.
        """
        try:
            # Ensure the directory exists
            self.file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)
            logger.info(f"Successfully saved {len(self.books)} books to {self.file_path}.")
        except Exception as e:
            logger.error(f"Error saving books to {self.file_path}: {e}")

    def add_book(self, book):
        """
        Adds a new Book object to the inventory.
        Checks for duplicate ISBNs.
        """
        if not isinstance(book, Book):
            logger.error("Attempted to add an object that is not a Book instance.")
            return False

        if any(b.isbn == book.isbn for b in self.books):
            logger.warning(f"Book with ISBN {book.isbn} already exists. Not adding duplicate.")
            return False
        self.books.append(book)
        self._save_books()
        logger.info(f"Book added: {book.title}")
        return True

    def search_by_title(self, title):
        """
        Searches for books by title (case-insensitive, partial match).

        Args:
            title (str): The title to search for.

        Returns:
            list: A list of Book objects matching the title.
        """
        matching_books = [book for book in self.books if title.lower() in book.title.lower()]
        if not matching_books:
            logger.info(f"No books found matching title: '{title}'")
        return matching_books

    def search_by_isbn(self, isbn):
        """
        Searches for a book by its ISBN.

        Args:
            isbn (str): The ISBN to search for.

        Returns:
            Book or None: The Book object if found, None otherwise.
        """
        for book in self.books:
            if book.isbn == isbn:
                return book
        logger.info(f"No book found with ISBN: '{isbn}'")
        return None

    def display_all(self):
        """
        Displays all books in the inventory.
        Returns True if books are displayed, False if inventory is empty.
        """
        if not self.books:
            print("The library inventory is empty.")
            return False
        print("\n--- Current Library Inventory ---")
        for book in self.books:
            print(book)
        print("-------------------------------")
        return True

# --- Task 4: Menu-Driven Command Line Interface ---
def get_valid_input(prompt, validator=None, error_message="Invalid input. Please try again."):
    """
    Helper function to get validated input from the user.
    """
    while True:
        user_input = input(prompt).strip()
        if validator:
            if validator(user_input):
                return user_input
            else:
                print(error_message)
                logger.warning(f"Invalid input received for '{prompt.strip()}': '{user_input}'")
        else:
            return user_input

def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Library Inventory Manager ---")
    print("1. Add New Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Books")
    print("6. Exit")
    print("---------------------------------")

def add_new_book(inventory):
    """
    Handles the process of adding a new book to the inventory.
    """
    print("\n--- Add New Book ---")
    title = get_valid_input("Enter title: ")
    author = get_valid_input("Enter author: ")
    isbn_validator = lambda x: bool(x) and len(x) > 0 # Simple non-empty check for ISBN
    isbn = get_valid_input("Enter ISBN: ", validator=isbn_validator, error_message="ISBN cannot be empty.")

    # Check if a book with this ISBN already exists
    if inventory.search_by_isbn(isbn):
        print(f"Error: A book with ISBN '{isbn}' already exists in the inventory.")
        logger.error(f"Attempted to add duplicate ISBN: {isbn}")
        return

    new_book = Book(title, author, isbn)
    if inventory.add_book(new_book):
        print(f"'{title}' by {author} (ISBN: {isbn}) added successfully.")
    else:
        print("Failed to add the book. See logs for details.")

def issue_book(inventory):
    """
    Handles the process of issuing a book.
    """
    print("\n--- Issue Book ---")
    isbn = get_valid_input("Enter ISBN of the book to issue: ")
    book = inventory.search_by_isbn(isbn)
    if book:
        if book.is_available():
            if book.issue():
                inventory._save_books() # Save changes after issuing
                print(f"Book '{book.title}' (ISBN: {isbn}) has been issued.")
                logger.info(f"Book issued: {book.title} (ISBN: {isbn})")
            else:
                print(f"Failed to issue book '{book.title}'. (Unexpected error)")
        else:
            print(f"Book '{book.title}' (ISBN: {isbn}) is already issued.")
            logger.warning(f"Attempted to issue an already issued book: {isbn}")
    else:
        print(f"No book found with ISBN: {isbn}")
        logger.warning(f"Attempted to issue non-existent book with ISBN: {isbn}")

def return_book(inventory):
    """
    Handles the process of returning a book.
    """
    print("\n--- Return Book ---")
    isbn = get_valid_input("Enter ISBN of the book to return: ")
    book = inventory.search_by_isbn(isbn)
    if book:
        if not book.is_available():
            if book.return_book():
                inventory._save_books() # Save changes after returning
                print(f"Book '{book.title}' (ISBN: {isbn}) has been returned.")
                logger.info(f"Book returned: {book.title} (ISBN: {isbn})")
            else:
                print(f"Failed to return book '{book.title}'. (Unexpected error)")
        else:
            print(f"Book '{book.title}' (ISBN: {isbn}) is already available.")
            logger.warning(f"Attempted to return an already available book: {isbn}")
    else:
        print(f"No book found with ISBN: {isbn}")
        logger.warning(f"Attempted to return non-existent book with ISBN: {isbn}")

def search_books(inventory):
    """
    Handles searching for books by title or ISBN.
    """
    print("\n--- Search Books ---")
    print("1. Search by Title")
    print("2. Search by ISBN")
    search_choice = get_valid_input("Enter your choice (1-2): ", lambda x: x in ['1', '2'], "Invalid choice. Please enter 1 or 2.")

    if search_choice == '1':
        title = get_valid_input("Enter title (partial match allowed): ")
        results = inventory.search_by_title(title)
        if results:
            print(f"\n--- Search Results for Title '{title}' ---")
            for book in results:
                print(book)
            print("---------------------------------------")
        else:
            print(f"No books found matching title: '{title}'")
    elif search_choice == '2':
        isbn = get_valid_input("Enter ISBN: ")
        result = inventory.search_by_isbn(isbn)
        if result:
            print(f"\n--- Search Result for ISBN '{isbn}' ---")
            print(result)
            print("-------------------------------------")
        else:
            print(f"No book found with ISBN: '{isbn}'")

def main():
    """
    Main function to run the command-line interface.
    """
    # Initialize LibraryInventory. The books.json will be created in the same directory as this script.
    inventory = LibraryInventory(file_path="books.json")

    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-6): ", lambda x: x in ['1', '2', '3', '4', '5', '6'], "Invalid choice. Please enter a number between 1 and 6.")

        try:
            if choice == '1':
                add_new_book(inventory)
            elif choice == '2':
                issue_book(inventory)
            elif choice == '3':
                return_book(inventory)
            elif choice == '4':
                inventory.display_all()
            elif choice == '5':
                search_books(inventory)
            elif choice == '6':
                print("Exiting Library Inventory Manager. Goodbye!")
                logger.info("Application exited.")
                break
        except Exception as e:
            logger.critical(f"An unhandled error occurred in the main loop: {e}", exc_info=True)
            print("An unexpected error occurred. Please check the logs.")

if __name__ == "__main__":
    main()