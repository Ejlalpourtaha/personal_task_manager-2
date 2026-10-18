# books.py

def display_books(books_list):
    """Display the list of books with their index."""
    print("\n--- Your Books List ---")
    if not books_list:
        print("No books found.")
    else:
        for index, book in enumerate(books_list, start=1):
            print(f"{index}. {book}")

def add_book_to_list(books_list, new_book):
    books_list.append(new_book)
    return books_list
