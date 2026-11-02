#ABOUT PROGRAM:
#The Library Book Program contains:
#1) Add books
# •	function to identify if added book id already exist.
#2)View books
# •	to check and show all available book in library.
# •	to show if the books are issued or available.
#3)Search books
# •	to search books in library through name or author
#4)Issue books
# •	to check whether the book is available or issued
# •	ask the name of the student borrowing it.
#5)Return book
# •	check whether the book is actually issued and return it to available book list.
#6)EXIT
# •	To exit the program.






# Library Book Issue System

# We create an empty list to store all the books.
# Every book that we add will be stored inside this list.
books = [
    {
        "id": "001",
        "name": "Python Programming",
        "author": "Mark Lutz",
        "issued": False,
        "issued_to": None
    },

    {
        "id": "002",
        "name": "Let Us C",
        "author": "Yashavant Kanetkar",
        "issued": False,
        "issued_to": None
    },

    {
        "id": "003",
        "name": "Data Structures",
        "author": "Seymour Lipschutz",
        "issued": False,
        "issued_to": None
    },

    {
        "id": "004",
        "name": "Computer Networks",
        "author": "Andrew S. Tanenbaum",
        "issued": False,
        "issued_to": None
    },

    {
        "id": "005",
        "name": "Database Management Systems",
        "author": "Raghu Ramakrishnan",
        "issued": False,
        "issued_to": None
    }
]
    
# ---------------------------------------------------------
# FUNCTION 1: ADD BOOK
# ---------------------------------------------------------

def add_book():

    # Ask the user to enter information about the book.
    book_id = input("Enter book ID: ")
    name = input("Enter book name: ")
    author = input("Enter author name: ")

    # Before adding the book, we check whether the ID already exists.
    # This prevents two books from having the same ID.
    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists!")
            return

    # A dictionary is used to store information about one book.
    # Each piece of information has a key and a value.
    book = {
        "id": book_id,
        "name": name,
        "author": author,

        # False means the book is currently available.
        "issued": False,

        # None means nobody has borrowed the book yet.
        "issued_to": None
    }

    # Add the new book dictionary to the books list.
    books.append(book)

    print("Book added successfully!")


# ---------------------------------------------------------
# FUNCTION 2: VIEW BOOKS
# ---------------------------------------------------------

def view_book():

    # Check whether there are any books in the library.
    if len(books) == 0:
        print("No books available in the library.")
        return

    # Go through every book in the books list.
    for book in books:

        print("----------------------------")
        print("Book ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])

        # Check whether the book is issued or available.
        if book["issued"] == True:
            print("Status: Issued")
            print("Issued To:", book["issued_to"])
        else:
            print("Status: Available")

    print("----------------------------")


# ---------------------------------------------------------
# FUNCTION 3: SEARCH BOOK
# ---------------------------------------------------------

def search_book():

    # Ask the user what book they want to search for.
    search = input("Enter book name or author to search: ")

    # This variable helps us know whether we found anything.
    found = False

    # Search through every book in the list.
    for book in books:

        # lower() makes the search easier.
        # For example, "python" and "Python" will both work.
        if search.lower() in book["name"].lower() or search.lower() in book["author"].lower():

            print("----------------------------")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])

            if book["issued"] == True:
                print("Status: Issued")
            else:
                print("Status: Available")

            print("----------------------------")

            # We found at least one matching book.
            found = True

    # If found is still False, there was no matching book.
    if found == False:
        print("Book not found.")


# ---------------------------------------------------------
# FUNCTION 4: ISSUE BOOK
# ---------------------------------------------------------

def issue_book():

    # Ask which book the user wants to issue.
    book_id = input("Enter book ID to issue: ")

    # Search for the book using its ID.
    for book in books:

        if book["id"] == book_id:

            # Check whether the book is already issued.
            if book["issued"] == True:
                print("This book is already issued.")
                return

            # Ask for the name of the student borrowing the book.
            student_name = input("Enter student name: ")

            # Change the book's status to issued.
            book["issued"] = True

            # Store the name of the student who borrowed it.
            book["issued_to"] = student_name

            print("Book issued successfully!")
            return

    # This message appears if no book with that ID was found.
    print("Book ID not found.")


# ---------------------------------------------------------
# FUNCTION 5: RETURN BOOK
# ---------------------------------------------------------

def return_book():

    # Ask for the ID of the book being returned.
    book_id = input("Enter book ID to return: ")

    # Search for the book.
    for book in books:

        if book["id"] == book_id:

            # Check whether the book is actually issued.
            if book["issued"] == False:
                print("This book is already available.")
                return

            # Change the status back to available.
            book["issued"] = False

            # Nobody currently has the book.
            book["issued_to"] = None

            print("Book returned successfully!")
            return

    # This message appears if the ID does not exist.
    print("Book ID not found.")


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

# while True keeps the library system running continuously.
# The loop only stops when the user chooses option 6.
while True:

    # Display the main menu.
    print("\n==============================")
    print("   Library Management System")
    print("==============================")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. EXIT")
    print("==============================")

    # Ask the user to select an option.
    choice = input("Enter your choice: ")

    # If the user enters 1, call the add_book function.
    if choice == "1":
        add_book()

    # If the user enters 2, call the view_book function.
    elif choice == "2":
        view_book()

    # If the user enters 3, call the search_book function.
    elif choice == "3":
        search_book()

    # If the user enters 4, call the issue_book function.
    elif choice == "4":
        issue_book()

    # If the user enters 5, call the return_book function.
    elif choice == "5":
        return_book()

    # If the user enters 6, break stops the while loop.
    elif choice == "6":
        print("Thank you for using the library system!")
        break

    # If the user enters anything else, show an error.
    else:
        print("Invalid choice!")
#Thankyou for reviewing the code.
#Regards,
#Shubham Karpe

