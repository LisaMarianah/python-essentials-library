# Library Management System - Lisa Hlongwane - Python Essentials 1


# Returns (total_copies, copies_available) across the whole library as a tuple
def library_totals(books):

    total_copies = 0
    copies_available = 0

    for book_id in books:
        total_copies += books[book_id]["total"]
        copies_available += books[book_id]["available"]

    return total_copies, copies_available

# Returns the book ID of the most-borrowed book, or None if no books
def most_borrowed(books):

    best_book = None
    highest = None

    for book_id in books:

        if highest is None or books[book_id]["times_borrowed"] > highest:
            highest = books[book_id]["times_borrowed"]
            best_book = book_id

    return best_book


# Asks for a number of copies, validates with try-except, returns int or None
def read_valid_copies():
    try:
        copies = int(input("Number of copies: "))

        if copies < 1:
            print("That is not a valid number of copies.")
            return None

        return copies

    except ValueError:
        print("That is not a valid number of copies.")
        return None

# Adds a new book OR adds copies to an existing title by the same author
def add_book(books, next_book_number):

    title = input("Title: ").strip()

    if title == "":
        print("Title cannot be blank.")
        return next_book_number

    author = input("Author: ").strip()

    if author == "":
        print("Author cannot be blank.")
        return next_book_number

    copies = read_valid_copies()

    if copies is None:
        return next_book_number

    # Check if the book already exists
    for book_id in books:

        if (books[book_id]["title"].lower() == title.lower() and
                books[book_id]["author"].lower() == author.lower()):

            books[book_id]["total"] += copies
            books[book_id]["available"] += copies

            print(
                "Added "
                + str(copies)
                + " more copies of "
                + book_id
                + ": "
                + title
                + " (now "
                + str(books[book_id]["total"])
                + " total)"
            )

            return next_book_number

    # Create a new book
    book_id = "B" + str(next_book_number)

    books[book_id] = {
        "title": title,
        "author": author,
        "total": copies,
        "available": copies,
        "times_borrowed": 0
    }

    print(
        "Added "
        + book_id
        + ": "
        + title
        + " by "
        + author
        + " ("
        + str(copies)
        + " copies)"
    )

    return next_book_number + 1

# Registers a new member with an empty borrowed list
def register_member(members, next_member_number):

    name = input("Name: ").strip()

    if name == "":
        print("Name cannot be blank.")
        return next_member_number

    member_id = "M" + str(next_member_number)

    members[member_id] = {
        "name": name,
        "borrowed": []
    }

    print("Registered " + member_id + ": " + name)

    return next_member_number + 1

# One member borrows one book - enforces ALL the rules, updates BOTH dicts
def borrow_book(books, members):

    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    book_id = input("Book ID: ").strip()

    if book_id not in books:
        print("No such book.")
        return

    if len(members[member_id]["borrowed"]) >= 3:
        print("A member may borrow at most 3 books.")
        return

    if book_id in members[member_id]["borrowed"]:
        print("That member already has this book.")
        return

    if books[book_id]["available"] == 0:
        print("No copies available.")
        return

    books[book_id]["available"] -= 1
    books[book_id]["times_borrowed"] += 1
    members[member_id]["borrowed"].append(book_id)

    print(
        member_id
        + " borrowed "
        + book_id
        + ": "
        + books[book_id]["title"]
        + " ("
        + str(books[book_id]["available"])
        + " of "
        + str(books[book_id]["total"])
        + " copies now available)"
    )
    
# One member returns one book - updates BOTH dicts
def return_book(books, members):

    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    book_id = input("Book ID: ").strip()

    if book_id not in books:
        print("No such book.")
        return

    if book_id not in members[member_id]["borrowed"]:
        print("That member does not have this book.")
        return

    members[member_id]["borrowed"].remove(book_id)
    books[book_id]["available"] += 1

    print(
        member_id
        + " returned "
        + book_id
        + ": "
        + books[book_id]["title"]
        + " ("
        + str(books[book_id]["available"])
        + " of "
        + str(books[book_id]["total"])
        + " copies now available)"
    )

# Case-insensitive keyword search over titles
def search_catalogue(books):

    if len(books) == 0:
        print("The catalogue is empty.")
        return

    keyword = input("Search for: ").strip().lower()

    found = False

    for book_id in books:

        info = books[book_id]

        if keyword in info["title"].lower():

            print(
                book_id
                + ": "
                + info["title"]
                + " by "
                + info["author"]
                + " - "
                + str(info["available"])
                + " of "
                + str(info["total"])
                + " available"
            )

            found = True

    if found == False:
        print("No books match that search.")

# Prints one member with the TITLES of their borrowed books
def member_summary(books, members):

    member_id = input("Member ID: ").strip()

    if member_id not in members:
        print("No such member.")
        return

    member = members[member_id]

    print(
        member_id
        + " - "
        + member["name"]
        + " | books out: "
        + str(len(member["borrowed"]))
        + " of 3 allowed"
    )

    if len(member["borrowed"]) == 0:
        print(" (no books out)")
        return

    for book_id in member["borrowed"]:

        book = books[book_id]

        print(
            " "
            + book_id
            + ": "
            + book["title"]
            + " by "
            + book["author"]
        )

# Prints the whole-library report
def library_report(books, members):

    if len(books) == 0:
        print("The catalogue is empty.")
        return

    total_copies, copies_available = library_totals(books)

    print("Library Report")
    print("----------------------------")
    print("Titles: " + str(len(books)))
    print("Total copies: " + str(total_copies))
    print("Copies available: " + str(copies_available))
    print("Copies on loan: " + str(total_copies - copies_available))

    best_book = most_borrowed(books)

    if best_book is not None:
        print(
            "Most borrowed: "
            + best_book
            + " - "
            + books[best_book]["title"]
            + " ("
            + str(books[best_book]["times_borrowed"])
            + " borrows)"
        )

    print("Registered members: " + str(len(members)))

    print("Members at 3-book limit:")

    found = False

    for member_id in members:

        if len(members[member_id]["borrowed"]) == 3:
            print(member_id + " - " + members[member_id]["name"])
            found = True

    if found == False:
        print("none")

# ---- main program ----

books = {}
members = {}

next_book_number = 1
next_member_number = 1

while True:
    print("\n LIBRARY MANAGEMENT SYSTEM ")
    print("----------------------------")
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
        next_book_number = add_book(books, next_book_number)

    elif choice == "2":
        next_member_number = register_member(members, next_member_number)

    elif choice == "3":
        borrow_book(books, members)

    elif choice == "4":
        return_book(books, members)

    elif choice == "5":
        search_catalogue(books)

    elif choice == "6":
        member_summary(books, members)

    elif choice == "7":
        library_report(books, members)

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1-8.")
