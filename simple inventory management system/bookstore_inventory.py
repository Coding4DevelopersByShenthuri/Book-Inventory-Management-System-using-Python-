# Inventory Management System for an Online Bookstore

# 1. Create an empty list named inventory to store dictionaries representing books.
inventory = []

# 2. Function to add a new book to the inventory
def add_book(inventory, new_book):
    for book in inventory:
        if book['title'].lower() == new_book['title'].lower() and book['author'].lower() == new_book['author'].lower():
            print("Error: This book already exists in the inventory.")
            return
    if new_book['price'] < 0 or new_book['quantity'] < 0:
        print("Error: Price and quantity must be non-negative.")
        return
    inventory.append(new_book)
    print(f"Book '{new_book['title']}' by {new_book['author']} added to inventory.")

# 3. Function to update an existing book in the inventory
def update_book(inventory, title):
    for book in inventory:
        if book['title'].lower() == title.lower():
            try:
                new_price = float(input("Enter the new price: "))
                new_quantity = int(input("Enter the new quantity: "))
                if new_price < 0 or new_quantity < 0:
                    print("Error: Price and quantity must be non-negative.")
                    return
                book['price'] = new_price
                book['quantity'] = new_quantity
                print(f"Book '{title}' updated.")
                return
            except ValueError:
                print("Error: Please enter valid numbers for price and quantity.")
                return
    print(f"Error: Book '{title}' not found in inventory.")

# 4. Function to search for books by keyword in title or author
def search_book(inventory, keyword):
    matches = []
    for book in inventory:
        if keyword.lower() in book['title'].lower() or keyword.lower() in book['author'].lower():
            matches.append(book)
    if matches:
        print("Matching books found:")
        for match in matches:
            print(f"Title: {match['title']}, Author: {match['author']}, Genre: {match['genre']}, "
                  f"Price: {match['price']}, Quantity: {match['quantity']}")
    else:
        print("No matching books found.")

# 5. Function to display all books in the inventory
def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for book in inventory:
        print(f"Title: {book['title']}, Author: {book['author']}, Genre: {book['genre']}, "
              f"Price: {book['price']}, Quantity: {book['quantity']}")

# 6. Main program loop to interact with the user
def main():
    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Update a book")
        print("3. Search for a book")
        print("4. Display inventory")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            try:
                price = float(input("Enter the book price: "))
                quantity = int(input("Enter the quantity in stock: "))
                new_book = {'title': title, 'author': author, 'genre': genre, 'price': price, 'quantity': quantity}
                add_book(inventory, new_book)
            except ValueError:
                print("Error: Please enter valid numbers for price and quantity.")
        
        elif choice == '2':
            title = input("Enter the title of the book to update: ")
            update_book(inventory, title)
        
        elif choice == '3':
            keyword = input("Enter a keyword to search for (in title or author): ")
            search_book(inventory, keyword)
        
        elif choice == '4':
            display_inventory(inventory)
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the main program loop
if __name__ == "__main__":
    main()
