# Book class definition
class Book:
    def __init__(self, book_id, title, author):
        # Initialize a book with id, title, and author
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        # String representation of a book
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}"


# Dictionary to store books with book_id as key
books = {}


# Function to add a new book
def create_book():
    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book ID already exists! Cannot add duplicate.")
    else:
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        new_book = Book(book_id, title, author)
        books[book_id] = new_book
        print("Book added successfully!")


# Function to display all books
def read_books():
    if not books:
        print("No books available.")
    else:
        print("\nList of Books:")
        for book in books.values():
            print(book)


# Function to update a book’s title and author
def update_book():
    book_id = input("Enter Book ID to update: ")
    if book_id in books:
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        books[book_id].title = title
        books[book_id].author = author
        print("Book updated successfully!")
    else:
        print("Book not found!")


# Function to delete a book by ID
def delete_book():
    book_id = input("Enter Book ID to delete: ")
    if book_id in books:
        del books[book_id]
        print("Book deleted successfully!")
    else:
        print("Book not found!")


# Function to search book by title (case-insensitive)
def search_by_title():
    title = input("Enter title to search: ").lower()
    found = False
    for book in books.values():
        if book.title.lower() == title:
            print(book)
            found = True
    if not found:
        print("No book found with that title.")


# Menu loop to interact with user
while True:
    print("\n===== BOOK CRUD MENU =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Book by Title")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_book()
    elif choice == "2":
        read_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        search_by_title()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")
