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
    ...
