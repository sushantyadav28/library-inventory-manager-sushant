from library_manager.inventory import LibraryInventory

lib = LibraryInventory()

while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        lib.add_book(title, author, isbn)
        print("Book added ")

    elif choice == "2":
        isbn = input("ISBN to issue: ")
        b = lib.search_by_isbn(isbn)
        if b and b.issue():
            lib.save_data()
            print("Book issued ")
        else:
            print("Cannot issue.")

    elif choice == "3":
        isbn = input("ISBN to return: ")
        b = lib.search_by_isbn(isbn)
        if b and b.return_book():
            lib.save_data()
            print("Book returned ")
        else:
            print("Cannot return.")

    elif choice == "4":
        for b in lib.all_books():
            print(b)

    elif choice == "5":
        title = input("Title to search: ")
        res = lib.search_by_title(title)
        if res:
            for b in res:
                print(b)
        else:
            print("No results found.")

    elif choice == "6":
        break

    else:
        print("Wrong choice.")
