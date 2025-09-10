def store_book(key, value):
    library[key] = value

def add_book():
    key = input("Enter the book ID to add: ")
    value = input("Enter the book name to add: ")
    library[key] = value
    print("Book added successfully!")

def remove_book():
    key = input("Enter the book ID to remove: ")
    if key in library:
        del library[key]
        print("Book removed successfully!")
    else:
        print("Book not found!")

def search_book():
    key = input("Enter the book ID to search: ")
    if key in library:
        print(f"Book found: {library[key]}")
    else:
        print("Book not found!")

def number_of_books():
    print("Number of books:", len(library))

def update_title():
    key = input("Enter the book ID to change: ")
    if key in library:
        value = input("New book title: ")
        library[key] = value
        print("Book updated successfully!")
    else:
        print("Book not found!")

def display():
    if library:
        for id, name in library.items():
            print(f"Book ID: {id} -> Book Name: {name}")
    else:
        print("No books in library.")

def check_title():
    value = input("Enter book title to check: ")
    if value in library.values():
        print("Book found!")
    else:
        print("Book not found!")

def option_input():
    while True:
        option = int(input("Enter a valid option: "))
        if option == 8:
            print("Exiting...")
            break
        option_search(option)

def option_search(option):
    match(option):
        case 1:
            add_book()
        case 2:
            remove_book()
        case 3:
            search_book()
        case 4:
            update_title()
        case 5:
            number_of_books()
        case 6:
            display()
        case 7:
            check_title()
        case _:
            print("Enter correct option!")


library = {}
n = int(input("Enter the number of entries: "))
for _ in range(n):
    book_id = input("Enter the book ID: ")
    book_title = input("Enter the book name: ")
    store_book(book_id, book_title)

print("\nOptions:")
print("1. Add book\n2. Remove book\n3. Search book\n4. Update book\n5. Count of books\n6. Display\n7. Check title\n8. Exit")

option_input()