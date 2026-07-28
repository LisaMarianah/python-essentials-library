# Library Management System - Lisa Hlongwane - Python Essentials 1


# Returns (total_copies, copies_available) across the whole library as a tuple
def library_totals(books):
    ...

# Returns the book ID of the most-borrowed book, or None if no books
def most_borrowed(books):
    ...

# Asks for a number of copies, validates with try-except, returns int or None
def read_valid_copies():
    ...

# Adds a new book OR adds copies to an existing title by the same author
def add_book(books):
    ...

# Registers a new member with an empty borrowed list
def register_member(members):
    ...

# One member borrows one book - enforces ALL the rules, updates BOTH dicts
def borrow_book(books, members):
    ...

# One member returns one book - updates BOTH dicts
def return_book(books, members):
    ...

# Case-insensitive keyword search over titles
def search_catalogue(books):
    ...

# Prints one member with the TITLES of their borrowed books
def member_summary(books, members):
    ...

# Prints the whole-library report
def library_report(books, members):
    ...

# ---- main program ----

books = {}
members = {}

next_book_number = 1
next_member_number = 1

while True:
    print("\n LIBRARY MANAGEMENT SYSTEM ")
    
    print("1. Add a book")
    print("2. Register a member")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Search the catalogue")
    print("6. Member summary")
    print("7. Library report")
    print("8. Exit")

    choice = input("Choose an option (1-8): ").strip()

    if choice == "1":
        print("Coming soon")

    elif choice == "2":
        print("Coming soon")

    elif choice == "3":
        print("Coming soon")

    elif choice == "4":
        print("Coming soon")

    elif choice == "5":
        print("Coming soon")

    elif choice == "6":
        print("Coming soon")

    elif choice == "7":
        print("Coming soon")

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1-8.")
